from django.http.response import JsonResponse
from app.formularios import AddAsistenciaForm
from django.views.generic.edit import CreateView
from app.models import Asistencia, Estudiante, Horarios
from django.shortcuts import render, HttpResponse
import datetime
def Asistencialist(request):
    data = {
        'estudiantes' : Estudiante.objects.all(),
        'horarios' : Horarios.objects.all(),
        'date' : datetime.datetime.now()
    }
    return render(request, 'views/asistencia/asistencia.html', data)
class AddAsistencia(CreateView):
    model = Asistencia
    template_name = ''
    form_class = AddAsistenciaForm
    success_url = '/asistencia/'
    def post(self, request, *args,**kwargs):
        data = {}
        try:
            form = self.form_class(request.POST)
            if form.is_valid():
                form.save()
            else:
                data['errors'] = form.errors
        except Exception as e:
            print('Errores : ', e)
        return JsonResponse(data, safe=False)
