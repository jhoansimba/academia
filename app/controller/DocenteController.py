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
        data = {}
        if form.is_valid():
            data['info'] = 'Success'
            form.save()
        else:
            print('Error ln-53: ', form.errors)
            data['error'] = 'Error: ' + str(form.errors)
        return JsonResponse(data , safe=False)
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
        save = ''
        code = ''
        for i in Notas.objects.all():
            save += str(i.id) + ','
        programa = [i for i in Programa.objects.filter(id = pro).exclude(nombre='Ninguno')]
        if programa:
            for i in programa:
                for j in Estudiante.objects.filter(id_programa = int(i.id)):
                    for k in MatriculaActual.objects.filter(nivel = nivel):
                        for l in k.asignacion.all():
                            if l == j:
                                try:
                                    # Existen notas de este estudiante registradas
                                    data.append({'notas': Notas.objects.get(estudiante_id = j.id_est).json()})
                                except Exception as e:
                                    # No existen notas de este estudiante registradas
                                    data.append(
                                        {'notas':{
                                            'code' : f'ID_{j.id_est}',
                                            'est': j,
                                            'estudiante': j.id_est,
                                            'p_nota1':0,
                                            'p_nota2':0,
                                            'p_nota3':0,
                                            's_nota1':0,
                                            's_nota2':0,
                                            's_nota3':0,
                                            't_nota1':0,
                                            't_nota2':0,
                                            't_nota3':0,
                                            'suma':0,
                                            'promedio':0,
                                            }
                                        }
                                    )
                                    code += f'ID_{j.id_est}' + ','
                                
        return render(request, 'views/docente/listadoEstudiantes.html', {'Estudiantes' : data, 'programa':pro, 'nivel':nivel, 'save': save, 'code' : code, 'name': 'Registro de notas', 'prog': [i.nombre for i in Programa.objects.filter(id = pro)]})
class Niveles(TemplateView):
    template_name="views/docente/listadoNiveles.html"
    def get_context_data(self, **kwargs):
        id = self.kwargs['programa']
        context  = super().get_context_data(**kwargs)
        context['niveles'] = [1,2,3,4,5,6,7]
        context['programa'] = id
        return context
class addNotas(CreateView):
    model = Notas
    form_class = editNotasEstudiante
    template_name = 'views/main.html'
    success_url = '/docentes/'
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        data = {}
        if form.is_valid():
            print('Registro Guardado: ')
            data['info'] = 'Success'
            form.save()
        else:
            print('Error ln-127 : ', form.errors)
            data['error'] = 'Error: ' + str(form.errors)
        return JsonResponse(data , safe=False)