from django.http.response import JsonResponse
from User.models import Paralelo
from django.views.generic.base import TemplateView
from app.Formularios.formAsignar import AsignaciondeNivel
from django.forms.models import ModelFormOptions
from app.Formularios.formAsistente import *
from app.mixin import PermisosUsuario
from app.Formularios.formSalud import AddSalud, FormSalud
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView
import datetime
from app.models import Comprobante, Estudiante, Ficha_salud, Horarios, Matricula, MatriculaActual, Numero, Programa, Talento_Humano
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


class MatriculaList(LoginRequiredMixin, ListView):
    permission_required = listado
    model = Modelo
    form_class = formulario
    template_name = templateName
    # template_name = '/estudiantes/'
    title = Title

    def get_context_data(self, **kwargs):
        data = []
        noMatriculados = ''
        for i in Estudiante.objects.all():
            nivel = ''
            fecha = ''
            matricula = ''
            id_comp = ''
            for j in MatriculaActual.objects.all():
                for k in j.asignacion.all():
                    if k == i:
                        nivel = j.nivel
            if Matricula.objects.filter(estudiante=i).exists():
                for j in Matricula.objects.filter(estudiante=i):
                    fecha = j.fecha
                    if j.matricula == True:
                        matricula = j.matricula
                        id_comp = j.id_comp
                    else:
                        noMatriculados += i.id_est + ','

            else:
                noMatriculados += i.id_est + ','
            data.append({'estudiante': i, 'nivel': nivel, 'fecha': fecha, 'matricula': matricula,
                        'id_comp': id_comp, 'comprobante': Comprobante.objects.filter(id_est = i)})
        print("data : " , data)
        context = super().get_context_data(**kwargs)
        context['name'] = ModeloTitulo
        context['object_list'] = data
        context['noMatriculados'] = noMatriculados
        context['date'] = datetime.datetime.now().strftime('%Y-%m-%d')

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
        context['estudiantes'] = Estudiante.objects.all()
        context['regresar'] = self.success_url
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        data = {}
        if form.is_valid():
            form.save()
            data['info'] = 'Guardado...'
        else:
            print('No Es válido: ', form.errors)
            data['error'] = 'Error...' + str(form.errors)

        return JsonResponse(data, safe=False)


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
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = f'Actualizar {ModeloTitulo}'
        context['regresar'] = URL
        return context


class HorariosList2(LoginRequiredMixin, ListView):
    permission_required = listado
    model = Cursos
    form_class = FormHorarios2
    template_name = 'views/Asistente/Horarios2.html'

    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Horarios'
      #  context['object_list'] = self.model.objects.filter(matricula = True)

        return context


class HorariosList(LoginRequiredMixin, ListView):
    permission_required = listado
    model = Programa
    form_class = FormHorarios
    template_name = 'views/Asistente/Horarios.html'

    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Horarios'
        context['object_list'] = Programa.objects.all().exclude(
            nombre='ninguno')

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
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = f'Actualizar {ModeloTitulo}'
        context['regresar'] = "../horarios"
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
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = f'Actualizar {ModeloTitulo}'
        context['regresar'] = "Horarios2"
        return context


class AsignarNiveles(LoginRequiredMixin, CreateView):
    model = MatriculaActual
    form_class = AsignaciondeNivel
    template_name = 'views/main.html'
    success_url = URL

    def get_context_data(self, **kwargs):
        curso = Estudiante.objects.filter(id_programa=None)
        programa = Estudiante.objects.filter(id_curso=None)
        data = []
        for i in Estudiante.objects.all():
            if i.id_programa.all():
                data.append(i)
        context = super().get_context_data(**kwargs)
        context['name'] = f'Agregar {ModeloTitulo}'
        context['programa'] = data
        context['regresar'] = self.success_url
        return context


class AsignarNivelesCurso(LoginRequiredMixin, CreateView):
    model = MatriculaActual
    form_class = AsignaciondeNivel
    template_name = 'views/main.html'
    success_url = URL

    def get_context_data(self, **kwargs):
        curso = Estudiante.objects.filter(id_programa=None)
        programa = Estudiante.objects.filter(id_curso=None)
        data = []
        for i in Estudiante.objects.all():
            if i.id_curso.all():
                data.append(i)
        context = super().get_context_data(**kwargs)
        context['name'] = f'Agregar {ModeloTitulo}'
        context['programa'] = data
        context['niveles'] = 'Niveles'
        context['regresar'] = self.success_url
        return context


class TalentoHumano(LoginRequiredMixin, ListView):
    permission_required = listado
    model = Talento_Humano
    form_class = FormHumano
    template_name = 'views/Asistente/TalentoHumano.html'

    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Horarios'
      #  context['object_list'] = self.model.objects.filter(matricula = True)

        return context


class addTalentoHumano (LoginRequiredMixin, CreateView):

    model = Talento_Humano
    form_class = FormHumano
    template_name = 'views/main.html'
    success_url = '/asistente/talentohumano'
    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Agregar Ficheros'
      #  context['object_list'] = self.model.objects.filter(matricula = True)

        return context


class editTalentoHumano(LoginRequiredMixin, UpdateView):

    model = Talento_Humano
    form_class = FormHumano
    template_name = 'views/main.html'
    success_url = '/asistente/talentohumano'

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return super().post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Actualizar Talento Humano'
        context['regresar'] = '/asistente/talentohumano'
        return context


class AsignacionListado(TemplateView):
    template_name = 'views/docente/listadoDocente.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Listado de Estudiantes'
        context['ruta'] = 'programa/'
        context['cursos_list'] = Programa.objects.all().exclude(nombre = 'ninguno')
        return context


class AsignacionPrograma(TemplateView):
    template_name = "views/Asistente/AsignacionParalelo.html"
    estudiantes = []

    def get_context_data(self, **kwargs):
        self.estudiantes = []
        id = self.kwargs['programa']
        for i in Estudiante.objects.filter(id_programa=id):
            for matricula in AsigacionParalelo.objects.filter(paralelo__programa_general__programa_id=id):
                for est in matricula.estudiantes.all():
                    if i == est:
                        self.estudiantes.append(est)
        context = super().get_context_data(**kwargs)
        context['numero'] = Numero.objects.all()
        context['programa'] = id
        context['object_list'] = AsigacionParalelo.objects.filter(
            paralelo__programa_general__programa_id=id)
        return context


class AgregarEstudiantes(CreateView):
    model = AsigacionParalelo
    form_class = AgregarEstudiantesForm
    template_name = 'views/main.html'
    success_url = '/asistente/programa/'
    estudiantes = []

    def dispatch(self, request, *args, **kwargs):
        self.success_url += self.kwargs['programa']
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        id = self.kwargs['programa']
        self.estudiantes = []
        for i in Estudiante.objects.filter(id_programa=id):
            for matricula in MatriculaActual.objects.all():
                for est in matricula.asignacion.all():
                    if i == est:
                        self.estudiantes.append(est)

        # print(estudiantes)
        context = super().get_context_data(**kwargs)
        context['regresar'] = '/asistente/programa/' + id
        context['paralelo'] = Paralelo.objects.filter(
            programa_general__programa_id=id)
        context['estudiantes'] = self.estudiantes
        return context
