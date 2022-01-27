from app.controller.CursosController import AsignacionCursos, AsignacionCursosAdd, addAsistenciaCurso
from app.models import Talento_Humano
from app.controller.AsistenteController import *
from app.controller.AsistenciaController import *
from app.controller.DocenteController import *
from app.controller.SaludController import *
from app.controller.EstudiantesController import *
from django.urls import path
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('representante/', login_required(listEstudiantes.as_view()), name='list_estudiantes'),
    path('representante/add', login_required(addEstudiuantes.as_view()), name='add_estudiantes'),
    path('representante/edit/<pk>', login_required(editEstudiuantes.as_view()), name='edit_estudiantes'),
    path('representante/listcomprobante/addComprobante', login_required(addComprobante.as_view()), name='comprobante_estudiantes'),
    path('representante/listcomprobante/', login_required(listComprobante.as_view()), name='comprobante_estudiantes'),
    path('representante/delete/<pk>',login_required(deleteEstudiuantes.as_view()), name='delete_estudiantes'),
    path('representante/comprobante/<pk>',login_required(ComprobanteView.as_view()), name='comprobante_estudiantes'),
     path('representante/comprobante/edit/<pk>', editComprobante.as_view(), name='edit_comprobante'),
    path('representante/salud', login_required(fichaSalud.as_view()), name='list_salud'),
    path('representante/addsalud', login_required(addSalud.as_view()), name='add_salud'),
     path('representante/salud/edit/<pk>', editSalud.as_view(), name='edit_salud'),
      path('representante/salud/delete/<pk>', deleteSalud.as_view(), name='delete_salud'),
    
    #Docente
    path('docentes/', DocenteView.as_view(), name='list_estudiantes_docente'),
    # path('docentes/add', login_required(addNotas.as_view()), name='addNotas'),
    path('docentes/programa/<programa>/nivel/<nivel>/getparalelo/<paralelo>/edit/<pk>', editNotas.as_view(), name='EDITNotas'),
    path('docentes/curso/<pk>/', addAsistenciaCurso.as_view(), name='asistencia_curso'),
    # path('edit/<pk>', editNotasEstudiantes.as_view(), name='NotasEdit'),
    #  path('docentes/listado/asistencia/add/<str:pro>', AddAsistencia.as_view(), name='add_asistencia'),
    # path('docentes/asistencia/add/<str:pro>', AddAsistencia.as_view(), name='add_asistencia'),
    path('docentes/programa/<programa>', Niveles.as_view(), name='listado_est'),
    # path('docentes/niveles/listado/<mt>/<pk>', Listado.as_view(), name='add_listado_est'),
   # path('docentes/programa/<programa>/nivel/<nivel>/', Listado.as_view(), name='add_listado_est'),
    path('docentes/programa/<programa>/nivel/<nivel>/getparalelo/', getParalelo.as_view(), name='get_paralelos'),
    path('docentes/programa/<programa>/nivel/<nivel>/getparalelo/<paralelo>/', Listado.as_view(), name='add_listado_est'),
     path('docentes/programa/<programa>/nivel/<nivel>/getparalelo/<paralelo>/asistencia', AsistenciaPro.as_view(), name='asistencia'),
    path('docentes/programa/<programa>/nivel/<nivel>/getparalelo/<paralelo>/add', addNotas.as_view(), name='add_listado_est'),
#Asistente
path('asistente/', MatriculaList.as_view() ,name='list_matricula'),
path('asistente/asignarprograma', AsignarNiveles.as_view() ,name='asignar_matricula_programa'),
path('asistente/asignarcursos', AsignarNivelesCurso.as_view() ,name='asignar_matricula_curso'),
path('asistente/talentohumano', TalentoHumano.as_view() ,name='Talento_Humano'),
path('asistente/talentohumano/add', addTalentoHumano.as_view() ,name='Add_Talento_Humano'),
path('asistente/talentohumano/edit/<pk>', editTalentoHumano.as_view() ,name='edit_Talento_Humano'),
path('asistente/add', addMatricula.as_view() ,name='add_matricula'),
path('asistente/edit/<pk>', editMatricula.as_view() ,name='edit_matricula'),
path('asistente/horarios', HorariosList.as_view() ,name='list_Horario'),
path('asistente/horarios2', HorariosList2.as_view() ,name='list_Horario2'),
path('asistente/editHorario/<pk>', editHorario.as_view() ,name='edit_Horario'),
path('asistente/editHorario2/<pk>', editHorario2.as_view() ,name='edit_Horario2'),
path('asistente/paralelo', ParaleloList.as_view() ,name='ParaleloList'),
path('asistente/paralelo/paralelo', addParalelo.as_view() ,name='addParalelo'),
path('asistente/periodo', PeriodoList.as_view() ,name='PeriodoList'),
path('asistente/periodo/add', addPeriodo.as_view() ,name='AddPeriodo'),
path('asistente/programageneral', ProgramaGeneralList.as_view() ,name='ProgramaGeneralList'),
path('asistente/programageneral/add', addProgramaGeneral.as_view() ,name='addProgramaGeneralList'),
path('asistente/asignacion', AsignacionListado.as_view() ,name='asignacion_p'),
path('asistente/asignacioncursos', AsignacionCursos.as_view() ,name='asignacion_c'),
path('asistente/asignacioncursos/add/<pk>', AsignacionCursosAdd.as_view() ,name='asignacion_c'),
path('asistente/programa/<programa>/', AsignacionPrograma.as_view(), name='programa_asistente'),
path('asistente/programa/<programa>/add', AgregarEstudiantes.as_view(), name='AgregarEstudiantes'),
path('getinfo/', getInfo.as_view(), name='getinfo'),
 
] 