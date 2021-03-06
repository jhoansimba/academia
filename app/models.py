from django.db.models.fields import CharField, DateField, TextField
from django.db.models.fields.files import ImageField
from django.forms.models import model_to_dict
from django.utils import tree
from django.utils.html import format_html
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.enums import ChoicesMeta

class Provincia (models.Model):
    id_provincia = models.AutoField(primary_key=True)
    nombre_provincia = models.CharField(max_length=11)
    def __str__(self) -> str:
        return '{}'.format(self.nombre_provincia)

class Ciudad (models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=11)
    id_provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return '{}'.format(self.nombre_ciudad)

class Direccion (models.Model):
    id_direc = models.AutoField(primary_key=True)
    calle1_direc = models.CharField(max_length=50)
    calle2_direc = models.CharField(max_length=50)
    id_ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def Direccion(self):
        txt = '{0}{1}{2}'
        return txt.format(self.calle1_direc, " y ", self.calle2_direc)

    def __str__(self) -> str:
        txt = '{0}{1}{2}'
        return txt.format(self.calle1_direc, " y ", self.calle2_direc)


class Representante (models.Model):

    cedula_rep = models.CharField(max_length=10, primary_key=True)
    nombres_rep = models.CharField(max_length=25)
    apellidos_rep = models.CharField(max_length=25)
    direccion_rep = models.ForeignKey(Direccion, on_delete=CASCADE)
    email_est = models.EmailField()
    telefono_est = models.CharField(max_length=10)
    parentezco_rep = models.CharField(max_length=10)

    def Representante(self):
        txt = '{0} {1} '
        return txt.format(self.nombres_rep, self.apellidos_rep)

    def __str__(self) -> str:
        txt = '{0} {1} '
        return txt.format(self.nombres_rep, self.apellidos_rep)


class Horarios (models.Model):
    id_horario = models.AutoField(primary_key=True)
    inicio_horario = models.TimeField()
    final_horario = models.TimeField()
    def json(self):
        txt = model_to_dict(self)
        return txt

    def Horario(self):
        txt = '{0}{1}{2}'
        return txt.format(self.inicio_horario, " a ", self.final_horario)

    def __str__(self) -> str:
        txt = '{0}{1}{2}'
        return txt.format(self.inicio_horario, " a ", self.final_horario)


class Numero(models.Model):
    nivel = models.CharField(verbose_name='Nivel N??mero #: ', max_length=1)
    def json(self):
        txt = model_to_dict(self)
        return txt
    def __str__(self) -> str:
        return '{}'.format(self.nivel)


class Niveles(models.Model):
    
    id = models.AutoField(primary_key=True)
    nivel = models.ForeignKey(Numero, on_delete=CASCADE)
    precio = models.FloatField()
    horario=models.ManyToManyField(Horarios)
    duracion = models.CharField(
        verbose_name='Duraci??n del Nivel: ', max_length=1, help_text='Duraci??n en meses')

    def json(self):
        txt = model_to_dict(self)
        txt['horario'] = self.horario.json()
        return txt
    def getHorarios(self):
        txt = ''
        for i in self.horario.all():
            txt += str(i) + '  '
        return txt
    def __str__(self) -> str:
        txt = ''
        for i in self.horario.all():
            txt += str(i) + '  '
        return '{}, horarios de: {}'.format(self.nivel, txt)


class Programa(models.Model):
    
    nombre = models.CharField(
        verbose_name='Nombre del Programa: ', unique=True, max_length=50)
    mensualidad = models.FloatField()
    imagen = models.ImageField(
        upload_to='images/programas/', verbose_name='Imagen del Programa')
    total = models.FloatField(null=True, blank=True, editable=False)
    nivel = models.ManyToManyField(Niveles)
    # horario=models.ForeignKey(Horarios,on_delete=CASCADE)
    # def json(self):
    #     txt = model_to_dict(self, exclude=['imagen', 'nivel'])
    #     return txt
    def json(self):
        txt = model_to_dict(self)
        return txt
    def __str__(self) -> str:
        return '{}'.format(self.nombre)


class Detalles(models.Model):
    id = models.AutoField(primary_key=True)
    detalle = models.CharField(
        verbose_name='Detalle del Curso ', max_length=50)
    valor = models.FloatField()

    def __str__(self) -> str:
        return '{} , {}'.format(self.detalle, self.valor)


class Cursos(models.Model):
    imagen_curso= models.ImageField(null=True, upload_to='images/cursos')
    horario= models.ForeignKey(Horarios, on_delete=CASCADE)
    nombre = models.CharField(
        verbose_name='Nombre del Programa: ', primary_key=True, max_length=50)
    detalle = models.ManyToManyField(Detalles)
   

    def __str__(self) -> str:
        return '{}'.format(self.nombre)


class Estudiante(models.Model):
    # id_est=models.AutoField(primary_key=True)
    id_est = models.CharField(
        max_length=10, primary_key=True, verbose_name='C??dula')
    imagen_est = models.ImageField(null=True,verbose_name='Fotograf??a', upload_to='images/estudiante',)
    nombres_est = models.CharField(max_length=25, verbose_name='Nombres')
    apellidos_est = models.CharField(max_length=25, verbose_name='Apellidos')
    # edad_est=models.DateField()
    fecha_est = models.DateField(verbose_name='Fecha Nacimiento')
    email_est = models.EmailField(verbose_name='Correo Electr??nico')
    telefono_est = models.CharField(max_length=10, verbose_name='N??mero de Telefono')
    id_rep = models.CharField(max_length=3, null=True, blank=True)
   # id_fichsal=models.ForeignKey(Ficha_salud,on_delete=models.CASCADE)
    id_curso = models.ManyToManyField(Cursos, null=True, blank=True, verbose_name='Cursos')
    id_programa = models.ManyToManyField(Programa, null=True, blank=True, verbose_name='Programas')
    id_direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE, verbose_name='Direcci??n Domiciliaria')

    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.nombres_est, self.apellidos_est)
    def __str__(self) -> str:
        txt = '{0} {1} '
        return txt.format(self.nombres_est, self.apellidos_est)
    def Representante(self):
        txt = '{0} {1} '
        return txt.format(self.representante.nombres_rep, self.representante.apellidos_rep)

    def Salud(self):
        txt = '{0} '
        return txt.format(self.salud.NomEnfer_fichsa)

    def Cursos(self):
        listado = ''
        for item in self.id_curso.all():
            listado += str(item) + ', '
        return '{}'.format(listado)
    def Programas(self):
        listado = ''
        for item in self.id_programa.all():
            listado += str(item) + ', '
        return '{}'.format(listado)
    def json(self):
        txt = model_to_dict(self, exclude=['imagen_est', 'id_curso', 'id_programa'])
        return txt
    def Direccion(self):
        txt = '{0}{1}{2}'
        return txt.format(self.direccion.calle1_direc, " y ", self.direccion.calle2_direc)


class Ficha_salud (models.Model):
    id_est = models.ForeignKey(Estudiante, on_delete=CASCADE)
    id_fichsal = models.AutoField(primary_key=True)
    NomEnfer_fichsa = models.CharField(max_length=11, verbose_name='Nombre de Enfermedad')
    descripcion_fichsal = models.TextField(verbose_name='Descripci??n')
    accionesTomar_fichsal = models.TextField(verbose_name='Acciones a tomar')
    telefonoEmer_fichsal = models.CharField(
        max_length=10, verbose_name='Tel??fono de emergencia')

    def Salud(self):
        txt = '{0}'
        return txt.format(self.NomEnfer_fichsa)

    def __str__(self) -> str:
        txt = '{0}'
        return txt.format(self.NomEnfer_fichsa)

    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.Estudiante.nombres_est, self.Estudiante.apellidos_est)


class Cargo (models.Model):
    id_car = models.AutoField(primary_key=True)
    nombre_car = models.CharField(max_length=15)

    def Cargo(self):
        txt = '{0}'
        return txt.format(self.nombre_car)

    def __str__(self) -> str:
        txt = '{0}'
        return txt.format(self.nombre_car)
def HojaDeVida(instance, filename):
    return 'file/talento_humano/{0}/HojadeVida/{1}'.format(instance.cedula_th, filename)
def CopiadeCedula(instance, filename):
    return 'file/talento_humano/{0}/Copia de Cedula/{1}'.format(instance.cedula_th, filename)
def CertificadoNoImpedimento(instance, filename):
    return 'file/talento_humano/{0}/Certificado de Impedimento/{1}'.format(instance.cedula_th, filename)
def CertificadoAntecedentes(instance, filename):
    return 'file/talento_humano/{0}/Certificado de antecedentes/{1}'.format(instance.cedula_th, filename)
def TitulosAcreditados(instance, filename):
    return 'file/talento_humano/{0}/Titulos acreditados/{1}'.format(instance.cedula_th, filename)
def CertificadosCapacitacion(instance, filename):
    return 'file/talento_humano/{0}/Certificados de Capacitacion/{1}'.format(instance.cedula_th, filename)
def ExperienciaLaboral(instance, filename):
    return 'file/talento_humano/{0}/Certificados de Experiencia laboral/{1}'.format(instance.cedula_th, filename)
def HistorialLaboral(instance, filename):
    return 'file/talento_humano/{0}/Historial Laboral/{1}'.format(instance.cedula_th, filename)
def CarnetDiscapacidad(instance, filename):
    return 'file/talento_humano/{0}/Carnet de discapacidad/{1}'.format(instance.cedula_th, filename)
def CertificacionBancaria(instance, filename):
    return 'file/talento_humano/{0}/Certificacion Bancaria/{1}'.format(instance.cedula_th, filename)
def Ruc(instance, filename):
    return 'file/talento_humano/{0}/Copia del RUC/{1}'.format(instance.cedula_th, filename)
    # return 'file/talento_humano/04016452221/Cedula)
class Talento_Humano (models.Model):
    imagen_th = models.ImageField(null=True, upload_to='images/talento_humano', verbose_name='Fotograf??a')
    cedula_th = models.CharField(
        max_length=10, primary_key=True, verbose_name='C??dula')
    nombres_th = models.CharField(max_length=25, verbose_name='Nombres')
    apellidos_th = models.CharField(max_length=25, verbose_name='Apellidos')
    cargo_th = models.ForeignKey(Cargo, on_delete=models.CASCADE, verbose_name='Cargo por el que postula')
    Fecha= models.DateField(verbose_name='Fecha de Entrega lista chequeo')
    telefono = models.CharField(max_length=10,verbose_name="Tel??fono")
    HojaVida= models.FileField(upload_to = HojaDeVida, verbose_name='1. Hoja de Vida')
    # HojaVida= models.FileField(upload_to='file/talento_humano/hoja de vida')
    CopiaCedula= models.FileField(upload_to=CopiadeCedula, verbose_name='2. Copia de la c??dula')
    CertiImpedimento= models.FileField(upload_to=CertificadoNoImpedimento , verbose_name='3. Certificado de no tener impedimento de trabajo')
    Antecedentes= models.FileField(upload_to=CertificadoAntecedentes, verbose_name='4. Certificado Antecedentes Penales')
    Titulos= models.FileField(upload_to=TitulosAcreditados, verbose_name='5. T??tulo que acredite su profesi??n')
    Experiencia= models.FileField(upload_to= ExperienciaLaboral, verbose_name='6. Certificados de experiencia laboral')
    Cursos= models.FileField(upload_to= CertificadosCapacitacion, verbose_name='7. Certificados de eventos de capacitaci??n en los ultimos 5 a??os')
    Historial= models.FileField(upload_to= HistorialLaboral, verbose_name='8. Impresi??n de historial Laboral ')
    CarnetDiscap= models.FileField(upload_to=CarnetDiscapacidad, verbose_name='9. Copia de carnet de discapcidad ')
    CertiBancaria= models.FileField(upload_to=CertificacionBancaria, verbose_name= '10. Certificaci??n Bancaria de la institucion financiera que corresponda')
    CopiaRuc= models.FileField(upload_to=Ruc, verbose_name='11. Copia de RUC')
    
   # id_curso=models.ManyToManyField(Cursos,verbose_name='Curso')
    id_direccion = models.ForeignKey(
        Direccion, on_delete=models.CASCADE, verbose_name='Direcci??n')
    def TalentoHumano(self):
        txt = '{0} {1} '
        return txt.format(self.nombres_th, self.apellidos_th)

    def __str__(self) -> str:
        txt = '{0} {1} '
        return txt.format(self.nombres_th, self.apellidos_th)


class Notas (models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=CASCADE)
    niveles = models.ForeignKey(
        Numero, on_delete=CASCADE, verbose_name='Seleccione el nivel')
    materia = models.ForeignKey(
        Programa, on_delete=CASCADE, verbose_name='Materia')
    parcial = models.CharField(
        choices=[('1', 'Uno')], default=1, max_length=1, verbose_name='Parcial', null=True)
    p_nota1 = models.FloatField(verbose_name='Trabajos', default=0, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    p_nota2 = models.FloatField(verbose_name='Tareas', default=0, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    p_nota3 = models.FloatField(verbose_name='examen', default=0, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])

    parcial2 = models.CharField(
        choices=[('1', 'Dos')], default=1, max_length=1, verbose_name='Parcial', null=True)
    s_nota1 = models.FloatField(verbose_name='Trabajos', default=0, blank=True, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    s_nota2 = models.FloatField(verbose_name='Tareas', default=0, blank=True, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    s_nota3 = models.FloatField(verbose_name='examen', default=0, blank=True, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    parcial3 = models.CharField(choices=[(
        '1', 'Tres')], default=1, blank=True, max_length=1, verbose_name='Parcial', null=True)
    t_nota1 = models.FloatField(verbose_name='Trabajos', default=0, blank=True, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    t_nota2 = models.FloatField(verbose_name='Tareas', default=0, blank=True, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    t_nota3 = models.FloatField(verbose_name='examen', default=0, blank=True, validators=[
                                MaxValueValidator(10), MinValueValidator(0)])
    sumatoria = models.FloatField(editable=False)
    promedio = models.FloatField(editable=False)
    estado = models.BooleanField(editable=False)

    def save(self, *args, **kwargs):
        self.sumatoria = self.SumaGeneral()
        self.promedio = self.Promedio()
        self.estado = self.EstadoEst()
        return super(Notas, self).save(*args, **kwargs)

    def json(self):
        datos = model_to_dict(self)
        datos['suma'] = self.SumaGeneral()
        datos['promedio'] = self.Promedio()
        datos['uno'] = self.SumaParcialUno()
        datos['dos'] = self.SumaParcialDos()
        datos['tres'] = self.SumaParcialTres()
        datos['materia'] = self.materia.nombre
        datos['estado'] = self.EstadoEst()
        datos['est'] = self.Estudiante()
        return datos

    def SumaParcialUno(self):
        suma = (self.p_nota1 + self.p_nota2 + self.p_nota3) / 3
        return round((suma), 2)

    def SumaParcialDos(self):
        suma = (self.s_nota1 + self.s_nota2 + self.s_nota3) / 3
        return round((suma), 2)

    def SumaParcialTres(self):
        suma = (self.t_nota1 + self.t_nota2 + self.t_nota3) / 3
        return round((suma), 2)

    def SumaGeneral(self):
        uno = Notas.SumaParcialUno(self)
        dos = Notas.SumaParcialDos(self)
        tres = Notas.SumaParcialTres(self)
        suma = uno + dos + tres
        return round(suma, 2)

    def Promedio(self):
        promedio = Notas.SumaGeneral(self) / 3
        return round(promedio, 2)

    def Estado(self):
        if Notas.SumaGeneral(self) > 20.5:
            return format_html("<spam style='color: green;' > Aprobado </spam>")
        else:
            return format_html("<spam style='color: red;' > Reprobado </spam>")

    def EstadoEst(self):
        if Notas.SumaGeneral(self) > 20.5:
            return True
        else:
            return False

    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.estudiante.nombres_est, self.estudiante.apellidos_est)

    def Cursos(self):
        txt = '{0}'
        return txt.format(self.curso_id.nombre_curso)
    def __str__(self) -> str:
        return '{}'.format(self.niveles)

class Comprobante (models.Model):
    i_comp = models.AutoField(primary_key=True)
    id_est = models.ForeignKey(Estudiante, on_delete=CASCADE, verbose_name="Estudiante")
    file_comp = models.FileField(null=True, upload_to='files/comprobante', verbose_name="Comprobante de pago")
    nivel_comp = models.ForeignKey(Numero, on_delete=CASCADE, verbose_name="Nivel",null=True, blank=True)

    def Estudiante(self):
        txt = '{0} {1} '
        return txt.format(self.Estudiante.nombres_est, self.Estudiante.apellidos_est)

    def comp(self):
        txt = '{0}{1}'
        return txt.format("comprobante de: ", self.id_est)
    def File(self):
        return '{}'.format(self.file_comp)

    def __str__(self) -> str:
        txt = '{}'
        return txt.format(self.id_est)


class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=CASCADE)
    # id_curso= models.ManyToManyField(Cursos)
    id_comp = models.ForeignKey(Comprobante, on_delete=CASCADE)
    fecha = models.DateField(verbose_name='Fecha de matr??cula')
    matricula = models.BooleanField(default=False)
    nivel = models.ForeignKey(Numero, on_delete=CASCADE, null=True, blank=True)

    def Curso(self):
        txt = []
        for i in self.estudiante.id_curso.all():
            txt.append(i.nombre)
        return txt
    def Programa(self):
        txt = []
        for i in self.estudiante.id_programa.all():
            txt.append(i.nombre)
        return txt

    def __str__(self) -> str:
        txt = []
        for i in self.estudiante.id_curso.all():
            print(i)
            # txt.append(i.id_curso)
        print(self.estudiante)
        return '{} {} {}'.format(self.estudiante, self.fecha, self.matricula)


class Asistencia (models.Model):
    id_asis = models.AutoField(primary_key=True)
    estudiante = models.ManyToManyField(Estudiante,blank=True,null=True)
    estado_asis = models.BooleanField()
    niveles = models.CharField(max_length=1, null = True, blank = True)
    categoria = models.CharField(max_length=1, null=True, blank= True)
    programaID = models.CharField(max_length=20, null=True, blank= True)
    fecha_asis = models.DateField(blank=True,null=True, verbose_name='Fecha de asistencia')
    horario_id = models.ForeignKey(
        Horarios, on_delete=CASCADE,blank=True,null=True, verbose_name='Hora')

    def Estudiante(self) -> str:
        txt = ''
        for i in self.estudiante.all():
            txt += i.nombres_est
        return txt
class MatriculaActual(models.Model):
    asignacion = models.ManyToManyField(Estudiante)
    nivel = models.ForeignKey(Numero, on_delete=CASCADE, null=True, blank=True)
    def __str__(self) -> str:
        return '{} {} {}'.format(self.asignacion,"a",self.nivel)
class ParametrosConstantes(models.Model):
    inicio = models.PositiveIntegerField(verbose_name="M??nimo de estudiantes")
    fin = models.PositiveIntegerField(verbose_name="M??ximo de estudiantes")
    descripcion = models.CharField(max_length=30)
    nombre = models.CharField(max_length=3)
    def __str__(self) -> str:
        return 'inicio: {}, fin: {}, descripcion: {}, nombre: {}'.format(self.inicio, self.fin, self.descripcion, self.nombre)
