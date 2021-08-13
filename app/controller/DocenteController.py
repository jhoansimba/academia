from json.encoder import JSONEncoder

from django.contrib.auth.mixins import LoginRequiredMixin
from app.mixin import PermisosUsuario
from app.Formularios.formNotas import addNotasEstudiante, editNotasEstudiante
from django.http.response import JsonResponse
from django.views.generic.base import TemplateView
from app.Formularios.formSalud import AddSalud
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from app.Formularios.formErtudiante import AddEstudiante, FormEstudiante
from app.models import Cursos, Estudiante,Ficha_salud, Notas
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
modelo = Notas
class DocenteView(LoginRequiredMixin,TemplateView):
   # permission_required = ('app.view_estudiante','app.delete_estudiantes')
    # model = Estudiante
    template_name = 'views/docente/listadoDocente.html'
    # template_name = '/estudiantes/'
    title = 'Lista de Estudiantes'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Listado de Estudiantes'
        context['object_list'] = Notas.objects.all()
        return context
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,  *args, **kwargs)
    def post(self, request,  *args, **kwargs):
        data = {}
        try:
            cursos = [i.nombre for i in Cursos.objects.filter(usuario__pk = self.request.user.pk)]
            action = request.POST['action']
            if action == 'listado':
                data = []
                opciones = ''
                for i in Notas.objects.filter(curso_id_id = cursos[0]):
                    data.append([
                        i.Estudiante(),
                        i.Cursos(),
                        i.SumaParcialUno(),
                        i.SumaParcialDos(),
                        i.SumaParcialTres(),
                        i.SumaGeneral(), 
                        i.Promedio(), 
                        i.EstadoEst(),
                        i.id,
                        opciones
                    ])
                return JsonResponse(data, safe=False)
            else:
                id = request.POST['id']
                data = Notas.objects.get(estudiante_id = id).json()

        except Exception as e:
            print('Error: ', e)
            data = {'error':'Estudiante sin Notas'}
        return JsonResponse(data, safe=False)

class addNotas(LoginRequiredMixin,PermisosUsuario, CreateView):
    permission_required = 'app.view_notas'
    model = modelo
    form_class = addNotasEstudiante 
    template_name = 'views/main.html'
    success_url = '/docentes/'
    def get_context_data(self, **kwargs):
        data = []
        cursos = [i.nombre for i in Cursos.objects.filter(usuario__pk = self.request.user.pk)]
        for i in Estudiante.objects.filter(id_curso = cursos[0]):
            x = Notas.objects.filter(estudiante__id_est = i.id_est).exists()
            if x == False:
                data.append({'id': i.id_est, 'name': i.Estudiante()})
        context = super().get_context_data(**kwargs)
        context['name'] = 'Agregar notas de Estudiantes'
        context['cursosUsuario'] = Cursos.objects.filter(usuario__pk = self.request.user.pk)
        context['estudianteAdd'] = data
        context['regresar'] = '/docentes/'
        return context
class editNotas(LoginRequiredMixin,UpdateView):
    model = Notas
    form_class = editNotasEstudiante
    template_name = 'views/main.html'
    success_url = '/docentes/'
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance = self.get_object())
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Actualizar Notas del Estudiante'
        context['regresar'] = '/docentes/'
        return context
