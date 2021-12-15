from django.contrib.auth.password_validation import password_changed
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.forms.models import model_to_dict
from django.utils import tree
from app.models import Cursos, Estudiante, MatriculaActual, Numero, Programa

 
class Usuario(AbstractUser):
    token = models.CharField(max_length=100, blank=True, null=True)
    curso = models.ManyToManyField(Cursos, blank=True, verbose_name=" " )
    programa = models.ManyToManyField(Programa, blank=True, verbose_name=" ")
    asignacionEstudiantes = models.ManyToManyField(Estudiante, blank=True, verbose_name="Asignación de Estudiantes ")
    
    def json(self):
        txt = model_to_dict(self)
        return txt
    def save(self, *args, **kwargs):
        print('Ver: ', self.password)
        if self.pk and len(self.password) < 50:
            self.set_password(self.password)
        if self.pk is None:
            psw = '_sha256$'
            password = str(self.password)
            if password.count(psw) == 0:
                self.set_password(self.password)
        return super().save(*args, **kwargs)
    def __str__(self) -> str:
        return '{} {}'.format(self.first_name, self.last_name)
class Periodo(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    def __str__(self) -> str:
        return '{}'.format(self.nombre)

class ProgramaGeneral(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete = CASCADE) 
    programa = models.ForeignKey(Programa, on_delete = CASCADE)
    def __str__(self) -> str:
            return 'periodo:{} -  {}'.format(self.periodo,self.programa)

class Paralelo(models.Model):
    programa_general = models.ForeignKey(ProgramaGeneral, on_delete = CASCADE) 
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    nivel = models.ForeignKey(Numero, on_delete= CASCADE)
    def __str__(self) -> str:
        return '{} | Nivel:  {} - {}'.format(self.programa_general, self.nivel, self.usuario)
    
class AsigacionParalelo(models.Model):
    paralelo= models.ForeignKey(Paralelo, on_delete = CASCADE)
    nombre = models.CharField(max_length=1, verbose_name="Nombre del paralelo")
    asignacionEstudiantes = models.ManyToManyField(MatriculaActual)
    def Nivel(self):
        return '{}'.format(self.paralelo.nivel)
    def Docente(self):
        return '{} {}'.format(self.paralelo.usuario.first_name, self.paralelo.usuario.last_name )
    def json(self):
        txt = model_to_dict(self)
        return txt
    def __str__(self) -> str:

        return 'paralelo:{}, {}'.format(self.nombre, self.paralelo)

class AsignacionCurso(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete = CASCADE)
    curso = models.ManyToManyField(Cursos)
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    def __str__(self) -> str:
        listado = ''
        for item in self.curso.all():
            listado += str(item) + ', '
        return '{}, {} {}'.format(self.periodo, listado, self.usuario)
class AsignacionCursoEstudiante(models.Model):
    asignacionCurso = models.ForeignKey(AsignacionCurso, on_delete = CASCADE)
    estudiantes = models.ManyToManyField(Estudiante)
    def __str__(self) -> str:
        listado = ''
        for item in self.estudiantes.all():
            listado += str(item) + ', '
        return '{}, {}'.format(self.asignacionCurso, listado)