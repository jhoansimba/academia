from django.utils.html import format_html
from app.models import *
from django.contrib import admin


# Register your models here.
admin.site.register(Notas)
# class Notas(admin.ModelAdmin):
#     list_display = ('Estudiante','Nivel','SumaParcialUno','SumaParcialDos','SumaParcialTres','SumaGeneral','Promedio','Estado')
#     def Nivel(self, obj):
#         return obj.niveles

@admin.register(Asistencia)
class Asistencia(admin.ModelAdmin):
    list_display = ('Estudiante','fecha_asis','estado_asis', 'categoria')
    search_fields = ('fecha_asis','estado_asis')
    list_filter = ('estado_asis','categoria')

@admin.register(Representante)
class Representante (admin.ModelAdmin):
    list_display=('Representante', 'cedula_rep', 'telefono_est', 'parentezco_rep')
admin.site.register(Ciudad )
admin.site.register(Direccion)
admin.site.register(Provincia)
admin.site.register(MatriculaActual)
admin.site.register(Horarios)
admin.site.register(Estudiante)
admin.site.register(Matricula)

@admin.register(Ficha_salud)
class Ficha_salud (admin.ModelAdmin):
    list_display=('id_est', 'Salud', 'descripcion_fichsal', 'accionesTomar_fichsal', 'telefonoEmer_fichsal')

admin.site.register(Talento_Humano)
admin.site.register(Cargo)

@ admin.register(Comprobante)
class Comprobante (admin.ModelAdmin):
    list_display=('Comprobante_sellado', 'id_est')
    def Comprobante_sellado(self, obj):
        return format_html("<h5> {0} </h5> ".format(obj.file_comp,))
admin.site.register(Programa)
admin.site.register(Numero)
admin.site.register(Cursos)
admin.site.register(Detalles)
admin.site.register(Niveles)
# admin.site.register(Aul)

