from django.db import models
from django.utils.html import format_html
from django.core import validators
from django.db import models
from django.db.models.base import Model
from django.db.models.deletion import CASCADE
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.enums import ChoicesMeta
from app.models import Asistencia, Cargo, Ciudad, Comprobante, Cursos, Direccion, Estudiante, Ficha_salud, Horarios, Matricula, Notas, Provincia, Representante
# Create your models here.
class Talento_Humano (models.Model):
   
   
    imagen_th=models.ImageField(null=True,upload_to='images/talento_humano')
    cedula_th=models.CharField(max_length=10, primary_key=True,verbose_name='Cedula')
    nombres_th=models.CharField(max_length=25, verbose_name='Nombres')
    apellidos_th=models.CharField(max_length=25, verbose_name='Apellidos')
    cargo_th=models.ForeignKey(Cargo, on_delete=models.CASCADE)
    email_est=models.EmailField(verbose_name='E-mail')
    telefono_est=models.CharField(max_length=10)
    id_curso=models.ForeignKey(Cursos,on_delete=models.CASCADE, verbose_name='Curso')
    id_direccion=models.ForeignKey(Direccion, on_delete=models.CASCADE, verbose_name='Dirección')
    def Talento_Humano(self):
        txt = '{0} {1} '
        return txt.format(self.nombres_th, self.apellidos_th)
    def __str__(self) -> str:
        txt = '{0} {1} '
        return txt.format(self.nombres_th, self.apellidos_th)
    def Cargo (self):
        txt = '{0}'
        return txt.format(self.Cargo.nombre_car)
