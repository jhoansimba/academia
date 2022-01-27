from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import request
from app.Formularios.formCursos import AddAsignacionCursoEstudiante
from User.models import AsignacionCurso, AsignacionCursoEstudiante
from app.Formularios.formAsistencia import AddAsistenciaForm
from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseRedirectBase, JsonResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from ..models import Asistencia, Cursos, Estudiante, Horarios, Programa
from django.db import models
from django.shortcuts import redirect, render, HttpResponse
from datetime import datetime

# cursos_model


class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('nombre').exclude(nombre='ninguno')
        return cursos

    def getcurso(idcurso):
        curso = Cursos.objects.get(id=idcurso)
        return curso


class programa_models():
    def programa_list():
        programa = Programa.objects.order_by('nombre')
        return programa

    def getcurso(idprograma):
        programa = Programa.objects.get(id_programa=idprograma)
        return programa
# CursosController


class CursosController():
    def index(request):
        cursos_list = Cursos_models.cursos_list()
        context = {'cursos_list': cursos_list}
        data = []
        for i in Cursos.objects.order_by('nombre').exclude(nombre='ninguno'):
            data.append({'ruta': '/cursos/', 'nombre': i.nombre,
                        'imagen': i.imagen_curso, 'horario': Horarios.objects.get(id_horario=i.horario_id)})

        for i in Programa.objects.order_by('nombre').exclude(nombre='ninguno'):
            data.append({'ruta': '/cursos/',
                        'nombre': i.nombre, 'imagen': i.imagen})
        return render(request,'views/docente/listadoDocente.html', {'cursos_list':data})

    def details(request, cursoid):
        object = Cursos_models.getcurso(cursoid)
        context = {'curso': object}
        return render(request, 'views/cursos/details.html', context)

    def obtener_curso(request):
        if request.method == 'POST':
            if request.user.is_authenticated:
                data = request.POST['id_curso']
                return HttpResponse('<h1>Jhoan Imbaquingo</h1>%s' % data)
            else:
                return HttpResponseRedirect('admin')


#class ProgramaController():
#    def index(request):
#        programa_list = programa_models.programa_list()
#        context = {'programa_list': programa_list}
#        return render(request, 'views/cursos/programa.html', context)

# consulta
# def getcursos(idcurso):
#    curso=Cursos.objects.get(id_curso=idcurso)
  #   for item in curso:
   #      Horario=Horarios.objects.get(id_horario=item.id_horario)


class AsignacionCursos(LoginRequiredMixin, TemplateView):
    template_name = 'views/Asistente/asignacion_curso.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Listado de Estudiantes'
        context['object_list'] = Estudiante.objects.filter()
        return context


class AsignacionCursosAdd(LoginRequiredMixin, CreateView):
    models = AsignacionCursoEstudiante
    form_class = AddAsignacionCursoEstudiante
    template_name = 'views/main.html'
    success_url = '/asistente/asignacioncursos'

    def get(self, request, *args, **kwargs):
        if Cursos.objects.filter(nombre=self.kwargs['pk']).exists() == False:
            return redirect(self.success_url)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['regresar'] = '/asistente/asignacioncursos'
        context['name'] = 'Agregar Curso'
        context['addCursos'] = AsignacionCurso.objects.filter(
            curso=self.kwargs['pk'])
        context['estudiantes'] = Estudiante.objects.filter(
            id_curso=self.kwargs['pk'])
        return context


class addAsistenciaCurso(CreateView):
    model = Asistencia
    form_class = AddAsistenciaForm
    template_name = 'views/asistencia/asistencia.html'
    success_url = '/docente/listado/'
    estudiante = []

    def get_context_data(self, **kwargs):
        ## AsignacionCursoEstudiante.objects.filter(asignacionCurso__curso = 'Música')
        print('PK: ', self.kwargs['pk'])
        estudiante = []
        for est in Estudiante.objects.filter(id_curso=self.kwargs['pk']):
            for asignacion in AsignacionCursoEstudiante.objects.filter(asignacionCurso__curso=self.kwargs['pk']):
                for i in asignacion.estudiantes.all():
                    if est == i:
                        estudiante.append(i)
        context = super().get_context_data(**kwargs)
        context['estudiantes'] = estudiante
        context['categoria'] = 'C'
        return context

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            curso = self.kwargs['pk']
            form = AddAsistenciaForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data['estudiante']
                form.cleaned_data['fecha_asis'] = datetime.now().strftime(
                    '%Y-%m-%d')
                for i in Estudiante.objects.filter(id_curso=curso):
                    if i in data:
                        est = Estudiante.objects.filter(id_est=i.id_est)
                        form.cleaned_data['estado_asis'] = True
                    else:
                        est = Estudiante.objects.filter(id_est=i.id_est)
                        form.cleaned_data['estado_asis'] = False
                    form.cleaned_data['estudiante'] = est
                    registro = AddAsistenciaForm(form.clean())
                    if registro.is_valid():
                        registro.save()
                    else:
                        print('Error no valido ln-138: ')
                        print(registro.errors)
                data = {'info': 'Datos Guardados'}
            else:
                print('Error Formulario no valido: ', form.errors)
                data = {'errors': 'Error uno ' + str(form.errors)}
        except Exception as e:
            print('Error Formulario l-145 : ', e)
            data = {'errors': 'Error ' + str(e)}
        return JsonResponse(data, safe=False)
