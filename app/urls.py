from app.controller.AsistenteController import HorariosList, HorariosList2, MatriculaList, addMatricula, editHorario, editHorario2, editMatricula
from app.controller.AsistenciaController import AddAsistencia, Asistencialist
from app.controller.DocenteController import *
from app.controller.SaludController import addSalud, deleteSalud, editSalud, fichaSalud
from app.controller.EstudiantesController import addComprobante, addEstudiuantes, deleteEstudiuantes, editEstudiuantes, listComprobante, listEstudiantes, Comprobante
from django.urls import path
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('representante/', login_required(listEstudiantes.as_view()), name='list_estudiantes'),
    path('representante/add', login_required(addEstudiuantes.as_view()), name='add_estudiantes'),
    path('representante/edit/<pk>', login_required(editEstudiuantes.as_view()), name='edit_estudiantes'),
    path('representante/listcomprobante/addComprobante', login_required(addComprobante.as_view()), name='comprobante_estudiantes'),
    path('representante/listcomprobante/', login_required(listComprobante.as_view()), name='comprobante_estudiantes'),
    path('representante/delete/<pk>',login_required(deleteEstudiuantes.as_view()), name='delete_estudiantes'),
    path('representante/comprobante/<pk>',login_required(Comprobante.as_view()), name='comprobante_estudiantes'),
    path('representante/salud', login_required(fichaSalud.as_view()), name='list_estudiantes'),
    path('representante/addsalud', login_required(addSalud.as_view()), name='add_salud'),
     path('representante/salud/edit/<pk>', login_required(editSalud.as_view()), name='edit_salud'),
      path('representante/salud/delete/<pk>', login_required(deleteSalud.as_view()), name='delete_salud'),
    
    #Docente
    path('docentes/', DocenteView.as_view(), name='list_estudiantes_docente'),
    path('docentes/add', login_required(addNotas.as_view()), name='addNotas'),
    path('docentes/edit/<pk>', login_required(editNotas.as_view()), name='EDITNotas'),
     path('docentes/asistencia/', Asistencialist, name='asistencia'),
    path('docentes/asistencia/add', AddAsistencia.as_view(), name='add_asistencia'),
#Asistente
path('asistente/', MatriculaList.as_view() ,name='list_matricula'),
path('asistente/add', addMatricula.as_view() ,name='add_matricula'),
path('asistente/edit/<pk>', editMatricula.as_view() ,name='edit_matricula'),
path('asistente/horarios', HorariosList.as_view() ,name='list_Horario'),
path('asistente/horarios2', HorariosList2.as_view() ,name='list_Horario2'),
path('asistente/editHorario/<pk>', editHorario.as_view() ,name='edit_Horario'),
path('asistente/editHorario2/<pk>', editHorario2.as_view() ,name='edit_Horario2')
 
] 