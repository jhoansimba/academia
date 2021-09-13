from app.Formularios.formAsistencia import AddAsistenciaForm
from django.http.response import JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import *
from app.models import Asistencia, Estudiante, Horarios, Programa
from django.shortcuts import render, HttpResponse
from datetime import datetime
from User.models import *
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
    est = ''
    horario = []
    def dispatch(self, request, *args, **kwargs):
        pro = self.kwargs['programa']
        n = self.kwargs['nivel']
        getHorario = Programa.objects.get(id = pro).nivel.all() # Horario
        horario = []
        for i in getHorario:
            nivel = '' + str(i.nivel)
            if nivel == n:
                for j in i.horario.all():
                    horario.append(j.json())
        self.horario = horario
        self.est = Estudiante.objects.filter(id_programa = pro).filter(matriculaactual__nivel = n)
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = self.est
        context['horarios'] = self.horario
        context['date'] = datetime.now()
        return context
    def post(self, request, *args, **kwargs):
        data = {}
        try:
            programa = self.kwargs['programa']
            n = self.kwargs['nivel']
            form = AddAsistenciaForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data['estudiante']
                form.cleaned_data['niveles'] = self.kwargs['nivel']
                pro = form.cleaned_data['horario_id'].id_horario
                form.cleaned_data['fecha_asis'] = datetime.now().strftime('%Y-%m-%d')
                for i in Estudiante.objects.filter(id_programa = programa).filter(matriculaactual__nivel = n):
                    if i in data:
                        est = Estudiante.objects.filter(id_est = i.id_est)
                        form.cleaned_data['estado_asis'] = True
                    else:
                        est = Estudiante.objects.filter(id_est = i.id_est)
                        form.cleaned_data['estado_asis'] = False
                    form.cleaned_data['estudiante'] = est
                    registro = AddAsistenciaForm(form.clean())
                    if registro.is_valid():
                        registro.save()
                    else:
                        print('Error no valido l-65: ')
                        print(registro.errors)
                data={'info' : 'Datos Guardados'}
            else:
                print('Error Formulario no valido: ', form.errors)
                data={'errors' : 'Error uno ' + str(form.errors)}
        except Exception as e:
            print('Error Formulario l-74 : ', e)
            data={'errors' : 'Error ' + str(e)}
        return JsonResponse(data, safe=False)