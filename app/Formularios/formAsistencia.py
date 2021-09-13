from django import forms
from app.models import Asistencia, Estudiante, MatriculaActual, Notas
from django.forms import ModelForm, widgets


class AddAsistenciaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['id_est'].widget.attrs['autofocus'] = True
        # self.fields['id_direccion'].widget.attrs['class'] = 'custom-select'
    class Meta:
        model = Asistencia
        fields = '__all__'
    
