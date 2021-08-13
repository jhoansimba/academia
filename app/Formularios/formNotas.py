from django import forms
from app.models import Estudiante, Notas
from django.forms import ModelForm, widgets


class addNotasEstudiante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['id_est'].widget.attrs['autofocus'] = True
        # self.fields['id_direccion'].widget.attrs['class'] = 'custom-select'
    class Meta:
        model = Notas
        fields = '__all__'
        
class editNotasEstudiante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['id_est'].widget.attrs['autofocus'] = True
        # self.fields['id_direccion'].widget.attrs['class'] = 'custom-select'
    class Meta:
        model = Notas
        fields = '__all__'
        exclude = ('estudiante','curso_id')