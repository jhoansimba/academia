from django.contrib.auth.mixins import LoginRequiredMixin
from app.mixin import PermisosUsuario
from app.Formularios.formSalud import AddSalud, FormSalud
from django.views.generic.edit import DeleteView, UpdateView
from django.views.generic.list import ListView

from app.models import Estudiante, Ficha_salud
from django.views.generic import CreateView


class fichaSalud(LoginRequiredMixin,ListView):
    model = Ficha_salud
    form_class = AddSalud
    template_name = 'views/estudiantes/listadoSalud.html'
    # template_name = '/estudiantes/'
    title = 'Salud'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Ficha de Salud'
        context['object_list'] = self.model.objects.filter(id_est__id_rep = self.request.user.pk)

        return context

class addSalud (LoginRequiredMixin,CreateView):
        model = Ficha_salud
        form_class = AddSalud
        template_name = 'views/main.html'
        success_url = '/representante/salud'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['name'] = 'Agregar Ficha'
            context['estudiantes'] = Estudiante.objects.filter(id_rep = self.request.user.pk)

            context['regresar'] = '/representante/salud'
            return context


class editSalud(LoginRequiredMixin,UpdateView):
    model = Ficha_salud
    form_class = FormSalud
    template_name = 'views/main.html'
    success_url = '/representante/salud'
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
        context['name'] = 'Actualizar ficha'
        context['regresar'] = '/representante/salud'
        return context

class deleteSalud(LoginRequiredMixin, DeleteView):
    permission_required = 'app.delete_estudiante'
    model = fichaSalud
    form_class = FormSalud
    template_name = 'views/main.html'
    success_url = '/representante/'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = 'Eliminar ficha'
        context['regresar'] = '/representante/salud'
        context['info'] = kwargs
        return context
