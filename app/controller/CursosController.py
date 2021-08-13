from django.http.response import HttpResponse, HttpResponseRedirect, HttpResponseRedirectBase
from ..models import Cursos, Horarios, Programa
from django.db import models
from django.shortcuts import render,HttpResponse

# cursos_model


class Cursos_models():
    def cursos_list():
        cursos = Cursos.objects.order_by('nombre')
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
       return render(request, 'views/cursos/cursos.html', context)
       

    def details(request, cursoid):
        object = Cursos_models.getcurso(cursoid)
        context = {'curso': object}
        return render(request, 'views/cursos/details.html', context)

    def obtener_curso(request):
        if request.method=='POST':
            if request.user.is_authenticated:
                 data=request.POST['id_curso']
                 return HttpResponse('<h1>Jhoan Imbaquingo</h1>%s' % data)
            else:
                return HttpResponseRedirect('admin')


class ProgramaController():
    def index(request):
       programa_list = programa_models.programa_list()
       context = {'programa_list': programa_list}
       return render(request, 'views/cursos/programa.html', context)
    
# consulta
# def getcursos(idcurso):
#    curso=Cursos.objects.get(id_curso=idcurso)
 #   for item in curso:
  #      Horario=Horarios.objects.get(id_horario=item.id_horario)
