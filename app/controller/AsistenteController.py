from django.forms.models import ModelFormOptions
from app.Formularios.formAsistente import *
from app.mixin import PermisosUsuario
from app.Formularios.formSalud import AddSalud, FormSalud
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from app.models import Estudiante, Ficha_salud, Horarios, Matricula, Programa
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
Modelo = Matricula
ModeloTitulo = 'Matrícula'
formulario = FormMatricula
formularioEdit = EditMatricula
templateName = 'views/Asistente/Matricula.html'
Title = f'Listado de {ModeloTitulo}'
URL = '/asistente/'
permisos = 'matricula'
listado = f'app.view_{permisos}'
agregar = f'app.add_{permisos}'
editar = f'app.chage_{permisos}'
eliminar = f'app.delete_{permisos}'
class MatriculaList( LoginRequiredMixin,ListView):
    permission_required = listado
    model = Modelo
    form_class = formulario
    template_name = templateName
    # template_name = '/estudiantes/'
    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = ModeloTitulo
        context['object_list'] = self.model.objects.filter(matricula = True)

        return context

class addMatricula (LoginRequiredMixin, CreateView):
       # permission_required = agregar
        model = Modelo
        form_class = formulario
        template_name = 'views/main.html'
        success_url = URL
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['name'] = f'Agregar {ModeloTitulo}'
            # context['estudiantes'] = Estudiante.objects.filter(id_rep = self.request.user.pk)

            context['regresar'] = self.success_url
            return context

class editMatricula(LoginRequiredMixin, PermisosUsuario, UpdateView):
    permission_required = editar
    model = Modelo
    form_class = formularioEdit
    template_name = 'views/main.html'
    success_url = URL
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
        context['name'] = f'Actualizar {ModeloTitulo}'
        context['regresar'] = URL
        return context

class HorariosList2( LoginRequiredMixin,ListView):
    permission_required = listado
    model = Cursos
    form_class = FormHorarios2
    template_name ='views/Asistente/Horarios2.html'
   
    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Horarios'
      #  context['object_list'] = self.model.objects.filter(matricula = True)

        return context

class HorariosList( LoginRequiredMixin,ListView):
    permission_required = listado
    model = Programa
    form_class = FormHorarios
    template_name ='views/Asistente/Horarios.html'
   
    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Horarios'
      #  context['object_list'] = self.model.objects.filter(matricula = True)

        return context



class editHorario(LoginRequiredMixin, UpdateView):
    permission_required = editar
    model = Programa
    form_class = FormHorarios
    template_name = 'views/main.html'
    success_url = '/asistente/horarios'
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
        context['name'] = f'Actualizar {ModeloTitulo}'
        context['regresar'] = URL
        return context

class editHorario2(LoginRequiredMixin, UpdateView):
    permission_required = editar
    model = Cursos
    form_class = FormHorarios2
    template_name = 'views/main.html'
    success_url = '/asistente/horarios'
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
        context['name'] = f'Actualizar {ModeloTitulo}'
        context['regresar'] = URL
        return context