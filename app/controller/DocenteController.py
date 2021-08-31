from json.encoder import JSONEncoder

from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from app.mixin import PermisosUsuario
from app.Formularios.formNotas import addNotasEstudiante, editNotasEstudiante
from django.http.response import JsonResponse
from django.views.generic.base import TemplateView, View
from app.Formularios.formSalud import AddSalud
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
from app.Formularios.formErtudiante import AddEstudiante, FormEstudiante
from app.models import Cursos, Estudiante,Ficha_salud, Matricula, MatriculaActual, Notas, Numero, Programa
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
        cursos = [i.nombre for i in Cursos.objects.filter(usuario__id = self.request.user.id).exclude(nombre='Ninguno')]
        programa = [i for i in Programa.objects.filter(usuario__id = self.request.user.id).exclude(nombre='Ninguno')]
        # print(programas)
        context = super().get_context_data(**kwargs)
        context['name'] = 'Listado de Estudiantes'
        context['cursos_list'] = programa
        return context
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,  *args, **kwargs)
  
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

class Listado(LoginRequiredMixin, TemplateView):
    template_name = 'listadoEstudiantes.html'
    def get(self, request, *args, **kwargs):
        data = []
        nivel = self.kwargs['nivel']
        pro = self.kwargs['programa']
        programa = [i for i in Programa.objects.filter(id = pro).exclude(nombre='Ninguno')]
        if programa:
            for i in programa:
                for j in Estudiante.objects.filter(id_programa = int(i.id)):
                    for k in MatriculaActual.objects.filter(nivel = nivel):
                        for l in k.asignacion.all():
                            if l == j:
                                data.append(j)  

        return render(request, 'views/docente/listadoEstudiantes.html', {'Estudiantes' : data, 'programa':pro})
class AddListado(LoginRequiredMixin,PermisosUsuario, CreateView):
    permission_required = 'app.view_notas'
    model = modelo
    form_class = addNotasEstudiante 
    template_name = 'views/main.html'
    success_url = '/docentes/programa/'
    def dispatch(self, request, *args, **kwargs):
        programa = self.kwargs['programa']
        nivel = self.kwargs['nivel']
        self.success_url = self.success_url + f'{programa}/nivel/{nivel}/'
        return super().dispatch(request, *args, **kwargs)
    def get_context_data(self, **kwargs):
        id = self.kwargs['pk']
        mt = self.kwargs['programa']
        est = Estudiante.objects.filter(id_est = id)
        existe = Notas.objects.filter(estudiante__id_est = id).exists()
        n = []
        if existe:
            for i in Numero.objects.all():
                notas = Notas.objects.filter(estudiante__id_est = id, niveles = i, materia = mt).exists()
                if notas == False:
                    n.append(i)
        else:
            n = [i for i in Numero.objects.all()]
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = Estudiante.objects.filter(id_est = id)
        context['nivel'] = n
        context['regresar'] = self.success_url
        context['materia'] = Programa.objects.filter(id = int(mt))
        return context
class Niveles(TemplateView):
    template_name="views/docente/listadoNiveles.html"
    
    def get_context_data(self, **kwargs):
        id = self.kwargs['programa']
        print('Programa : ', id)
        context  = super().get_context_data(**kwargs)
        context['niveles'] = [1,2,3,4,5,6,7]
        context['programa'] = id
        return context