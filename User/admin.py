from User.models import AsigacionParalelo, Paralelo, Periodo, ProgramaGeneral, Usuario, AsignacionCurso, AsignacionCursoEstudiante
from django.contrib import admin

# Register your models here.

admin.site.register(Periodo)
admin.site.register(Usuario)
admin.site.register(ProgramaGeneral)
admin.site.register(Paralelo)
admin.site.register(AsigacionParalelo)
admin.site.register(AsignacionCurso)
admin.site.register(AsignacionCursoEstudiante)