from django.http.response import JsonResponse
from django.shortcuts import render
from User.models import AsignacionCurso, Paralelo, Periodo
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
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from academia21 import settings
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


class MatriculaList(LoginRequiredMixin, TemplateView):
    template_name = templateName
    title = Title

    def get_context_data(self, **kwargs):
        data = []
        noMatriculados = ''
        for matriculaActual in MatriculaActual.objects.all():
            estudiantes = []
            for est in matriculaActual.asignacion.all():
                print('Estudiante: ', est)
                matricula = Matricula.objects.filter(estudiante=est, nivel=matriculaActual.nivel).first() if Matricula.objects.filter(
                    estudiante=est, nivel=matriculaActual.nivel).exists() else ''
                comprobante = Comprobante.objects.filter(
                    id_est=est) if Comprobante.objects.filter(id_est=est).exists() else ''
                noMatriculados += est.id_est + f'-{matriculaActual.nivel},'
                estudiantes.append({'estudiante': est, 'matricula': matricula,
                                   'comprobante': comprobante, 'nivel': matriculaActual.nivel})
            if estudiantes:
                data.append({
                    'asignacion': estudiantes,
                })
        context = super().get_context_data(**kwargs)
        context['object_data'] = data
        context['name'] = 'Matrícula de Estudiantes'
        context['date'] = datetime.datetime.now().strftime('%Y-%m-%d')
        context['noMatriculados'] = noMatriculados
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
        context['regresar'] = "/asistente/horarios2"
        return context


class getInfo(TemplateView):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,  *args, **kwargs)

    def post(self, request, *args, **kwargs):
        materia = ''
        nivel = ''
        data = []
        idAsignacion = ''
        programa = ''
        idParalelo = ''
        opcionEst = ''
        try:
            materia = request.POST['materia']
        except:
            pass
        try:
            materia = request.POST['materia']
            opcionEst = request.POST['opcion']
        except:
            pass
        try:
            nivel = request.POST['nivel']
        except:
            pass
        try:
            idAsignacion = request.POST['id']
            programa = request.POST['programa']
        except:
            pass
        try:
            idParalelo = request.POST['id_paralelo']
            programa = request.POST['programa']
        except:
            pass
        if materia and nivel:
            matriculados = []
            for matricula in MatriculaActual.objects.filter(nivel=nivel):
                for estudiantes in matricula.asignacion.all():
                    matriculados.append(estudiantes)
            if matriculados:
                for estudiantes in Estudiante.objects.filter(id_programa=materia):
                    if estudiantes not in matriculados:
                        data.append({'estudiantes': estudiantes.json()})
            else:
                for estudiantes in Estudiante.objects.filter(id_programa=materia):
                    data.append({'estudiantes': estudiantes.json()})
        if materia and opcionEst:
            matriculados = []
            for matricula in MatriculaActual.objects.filter(nivel=None):
                for estudiantes in matricula.asignacion.all():
                    matriculados.append(estudiantes)
            if matriculados:
                for estudiantes in Estudiante.objects.filter(id_curso=materia):
                    if estudiantes not in matriculados:
                        data.append({'estudiantes': estudiantes.json()})
            else:
                for estudiantes in Estudiante.objects.filter(id_curso=materia):
                    data.append({'estudiantes': estudiantes.json()})
        if idAsignacion:
            for matricula in MatriculaActual.objects.filter(id=idAsignacion):
                for estudiantes in matricula.asignacion.all():
                    for est in Estudiante.objects.filter(id_programa=programa):
                        if est == estudiantes:
                            data.append({'est': estudiantes.Estudiante()})

        if idParalelo:
            lista = []
            for i in AsigacionParalelo.objects.all():
                for j in i.asignacionEstudiantes.all():
                    lista.append(j.id)
            paralelo = Paralelo.objects.get(id=idParalelo)
            for i in MatriculaActual.objects.all():
                val = False
                for j in i.asignacion.all():
                    for k in Estudiante.objects.filter(id_programa=programa):
                        if k == j and i.nivel == paralelo.nivel:
                            val = True
                if val and i.id not in lista:
                    data.append({'id': i.id, 'nivel': str(i.nivel),
                                'size': str(len(i.asignacion.all()))})
        return JsonResponse(data, safe=False)


class AsignarNiveles(LoginRequiredMixin, CreateView):
    model = MatriculaActual
    form_class = AsignaciondeNivel
    template_name = 'views/main.html'
    success_url = URL

    def get_context_data(self, **kwargs):
        data = []
        matriculados = []
        noMatriculados = []
        for matricula in MatriculaActual.objects.all():
            for estudiantes in matricula.asignacion.all():
                matriculados.append({'etudiantes': estudiantes})
        if matriculados:
            for estudiantes in Estudiante.objects.all():
                if estudiantes not in matriculados:
                    data.append({'etudiantes': estudiantes})
        else:
            for estudiantes in Estudiante.objects.all():
                data.append({'etudiantes': estudiantes})
        context = super().get_context_data(**kwargs)
        context['name'] = f'Agregar {ModeloTitulo}'
        context['programa'] = data
        context['materia'] = Programa.objects.all().exclude(nombre='ninguno')
        context['nivel'] = Numero.objects.all()
        context['tipoOpcion'] = 'Materia'
        context['descripcion'] = 'Nivel'
        context['regresar'] = self.success_url
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        try:
            if form.is_valid():
                asignacion = form.cleaned_data['asignacion']
                print('Asignacipon: ', asignacion)
                if len(asignacion) >= int(settings.DESDE) and len(asignacion) <= int(settings.HASTA):  # rango para matrículas
                    return super().post(request, *args, **kwargs)
                else:
                    data = []
                    for i in Estudiante.objects.all():
                        if i.id_programa.all():
                            data.append(i)
                    return render(self.request, self.template_name, {'form': self.form_class, 'descripcion': 'Nivel','tipoOpcion': 'Materia' ,'errores': f'Verifique que el número de estudiantes sea {settings.DESDE} o {settings.HASTA}, usted ha seleccionado {len(asignacion)}', 'programa': data, 'materia': Programa.objects.all().exclude(nombre='ninguno'), 'nivel': Numero.objects.all()})
        except Exception as e:
            print(f'Error en el método AsignarNiveles:{form}, error: {e}')


class AsignarNivelesCurso(LoginRequiredMixin, CreateView):
    model = MatriculaActual
    form_class = AsignaciondeNivel
    template_name = 'views/main.html'
    success_url = URL

    def get_context_data(self, **kwargs):
        data = []
        for i in Estudiante.objects.all():
            if i.id_curso.all():
                data.append(i)
        context = super().get_context_data(**kwargs)
        context['name'] = f'Agregar {ModeloTitulo}'
        context['programa'] = data
        context['materia'] = Cursos.objects.all().exclude(nombre='ninguno')
        context['niveles'] = 'Niveles'
        context['tipoOpcion'] = 'Curso'
        context['descripcion'] = 'Estudiantes'
        context['regresar'] = self.success_url
        return context
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        try:
            if form.is_valid():
                asignacion = form.cleaned_data['asignacion']
                print('Asignacipon: ', asignacion)
                if len(asignacion) >= settings.DESDE and len(asignacion) <= settings.HASTA:  # rango para matrículas
                    return super().post(request, *args, **kwargs)
                else:
                    data = []
                    for i in Estudiante.objects.all():
                        if i.id_programa.all():
                            data.append(i)
                    return render(self.request, self.template_name, {'form': self.form_class, 'descripcion': 'Estudiantes','tipoOpcion': 'Curso' ,'errores': f'Verifique que el número de estudiantes sea 3 o 6, usted ha seleccionado {len(asignacion)}', 'programa': data, 'materia': Cursos.objects.all().exclude(nombre='ninguno'), 'nivel': Numero.objects.all()})
        except Exception as e:
            print(f'Error en el método AsignarNivelesCurso:{form}, error: {e}')


class TalentoHumano(LoginRequiredMixin, ListView):
    permission_required = listado
    model = Talento_Humano
    form_class = FormHumano
    template_name = 'views/Asistente/TalentoHumano.html'

    title = "Periodos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Horarios'
      #  context['object_list'] = self.model.objects.filter(matricula = True)

        return context


class PeriodoList(LoginRequiredMixin, ListView):
    permission_required = listado
    model = Periodo
    form_class = FormPeriodo
    template_name = 'views/Asistente/Periodo.html'

    title = "Periodos"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Periodos'

        return context
class ProgramaGeneralList(LoginRequiredMixin, ListView):
    permission_required = listado
    model = ProgramaGeneral
    form_class = FormProgramaGeneral
    template_name = 'views/Asistente/ProgramaGeneral.html'

    title = "Programa General"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Programa General'

        return context
class ParaleloList(LoginRequiredMixin, ListView):
   permission_required = listado
   model = Paralelo
   form_class = FormParalelo
   template_name = 'views/Asistente/Docenteparalelo.html'
   title = Title
   def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context['name2'] = 'Asignacion Docente'
     #  context['object_list'] = self.model.objects.filter(matricula = True)
       return context


class addPeriodo (LoginRequiredMixin, CreateView):
    
    model = Periodo
    form_class = FormPeriodo
    template_name = 'views/main.html'
    success_url = '/asistente/periodo'
    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Agregar periodo'
        context['regresar'] = '/asistente/periodo'
     #  context['object_list'] = self.model.objects.filter(matricula = True)
        return context
class addProgramaGeneral (LoginRequiredMixin, CreateView):
    
    model = ProgramaGeneral
    form_class = FormProgramaGeneral
    template_name = 'views/main.html'
    success_url = '/asistente/programageneral'
    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Agregar Programa General'
        context['regresar'] = '/asistente/programageneral'
     #  context['object_list'] = self.model.objects.filter(matricula = True)
        return context
class addParalelo (LoginRequiredMixin, CreateView):

    model = Paralelo
    form_class = FormParalelo
    template_name = 'views/main.html'
    success_url = '/asistente/paralelo'
    title = Title

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Agregar Programa General'
        context['regresar'] = '/asistente/paralelo'
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
        context['cursos_list'] = Programa.objects.all().exclude(
            nombre='ninguno')
        return context


class AsignacionPrograma(TemplateView):
    template_name = "views/Asistente/AsignacionParalelo.html"
    estudiantes = []

    def get_context_data(self, **kwargs):
        id = self.kwargs['programa']
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
        data = []
        paralelos = []
        for j in AsigacionParalelo.objects.all():
            data.append(j.paralelo)
        for i in Paralelo.objects.filter(programa_general__programa_id=id):
            if i not in data:
                paralelos.append(i)

        self.estudiantes = []
        data = []
        for i in Estudiante.objects.filter(id_programa=id):
            for matricula in MatriculaActual.objects.all():
                for est in matricula.asignacion.all():
                    if i == est:
                        self.estudiantes.append(est)
        context = super().get_context_data(**kwargs)
        context['regresar'] = '/asistente/programa/' + id
        context['paralelo'] = paralelos
        context['programa'] = id
        context['name'] = 'Asignación de Paralelo'
        context['estudiantes'] = self.estudiantes
        return context
