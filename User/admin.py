from User.models import AsigacionParalelo, Paralelo, Periodo, ProgramaGeneral, Usuario
from django.contrib import admin

# Register your models here.

admin.site.register(Periodo)
admin.site.register(Usuario)
admin.site.register(ProgramaGeneral)
admin.site.register(Paralelo)
admin.site.register(AsigacionParalelo)