from app.Formularios.formAsistencia import AddAsistenciaForm
from django.http.response import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import *
from app.models import Asistencia, Estudiante, Horarios, Niveles, Programa
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime
from User.models import *
from .service import getTime 
def Asistencialist(request):
    
    data = {
        'estudiantes' : Estudiante.objects.all(),
        'horarios' : Horarios.objects.all(),
        'date' : datetime.now()
    }
    return render(request, 'views/asistencia/asistencia.html', data)

class AsistenciaPro(LoginRequiredMixin,CreateView):
    model = Asistencia
    form_class = AddAsistenciaForm
    template_name = 'views/asistencia/asistencia.html'
    success_url = '/docente/listado/'
    est = []
    horario = []
  
    def dispatch(self, request, *args, **kwargs):
        self.est = []
        nivel = self.kwargs['nivel']
        pro = self.kwargs['programa']
        par = self.kwargs['paralelo']
        # validacion = AsigacionParalelo.objects.filter(paralelo__usuario_id= self.request.user.id).filter(paralelo__nivel=nivel).order_by('nombre').filter(paralelo__programa_general__programa=pro).filter(nombre = par)
        for items in AsigacionParalelo.objects.filter(paralelo__usuario_id= self.request.user.id).filter(paralelo__nivel_Paralelo=nivel).order_by('nombre').filter(paralelo__programa_general__programa=pro).filter(nombre = par):
            for est in items.asignacionEstudiantes.all():
                for asignacion in est.asignacion.all():
                    self.est.append(asignacion)
        getHorario = Programa.objects.get(id = pro).nivel.all() # Horario
        horario = []
        for i in getHorario:
            nivel = '' + str(i.nivel)
            if nivel == nivel:
                for j in i.horario.all():
                    horario.append(j.json())
        self.horario = horario
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = self.est
        context['horarios'] = self.horario
        context['date'] = datetime.now()
        context['categoria'] = 'P'
        context['horario'] = 'True'

        return context
    def get(self, request, *args, **kwargs):
        nivel = self.kwargs['nivel']
        pro = self.kwargs['programa']
        par = self.kwargs['paralelo']
        validacion = AsigacionParalelo.objects.filter(paralelo__usuario_id= self.request.user.id).filter(paralelo__nivel_Paralelo=nivel).order_by('nombre').filter(paralelo__programa_general__programa=pro).filter(nombre = par).exists()
        if validacion == False:
            return redirect(f'/docentes/programa/{pro}')
        return super().get(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            programa = self.kwargs['programa']
            n = self.kwargs['nivel']
            par = self.kwargs['paralelo']
            form = AddAsistenciaForm(request.POST)
            if form.is_valid():
                fechaActual = getTime()
                data = form.cleaned_data['estudiante']
                form.cleaned_data['niveles'] = n
                horarioID = form.cleaned_data['horario_id'].id_horario
                form.cleaned_data['fecha_asis'] = fechaActual['datetime'].split('T')[0]
                listaEstudiantes = []
                if(Asistencia.objects.filter(niveles = n).filter(programaID = programa).filter(fecha_asis = fechaActual['datetime'].split('T')[0]).filter(horario_id = horarioID).exists() == False) :
                    for i in AsigacionParalelo.objects.filter(paralelo__nivel_Paralelo = n).filter(paralelo__usuario = self.request.user.id).filter(paralelo__programa_general__programa = programa).filter(nombre = par):
                        for j in i.asignacionEstudiantes.all():
                            for k in j.asignacion.all():
                                listaEstudiantes.append(k)
                    for i in listaEstudiantes: #Estudiante.objects.filter(id_programa = programa).filter(matriculaactual__nivel = n):
                        if i in data:
                            est = Estudiante.objects.filter(id_est = i.id_est)
                            form.cleaned_data['estado_asis'] = True
                        else:
                            est = Estudiante.objects.filter(id_est = i.id_est)
                            form.cleaned_data['estado_asis'] = False
                        form.cleaned_data['estudiante'] = est
                        form.cleaned_data['programaID'] = f'P{programa}'

                        registro = AddAsistenciaForm(form.clean())
                        if registro.is_valid():
                            registro.save()
                        else:
                            print('Error no valido l-65: ')
                            print(registro.errors)
                    data={'info' : 'Datos Guardados'}
                else:
                    data={'errors' : 'Ya se ha registrado asistencia este d??a'}
            else:
                print('Error Formulario no valido: ', form.errors)
                data={'errors' : 'Error uno ' + str(form.errors)}
        except Exception as e:
            print('Error Formulario l-74 : ', e)
            data={'errors' : 'Error ' + str(e)}
        return JsonResponse(data, safe=False)