from User.models import AsignacionCurso, AsignacionCursoEstudiante
from django import forms
from django.forms import ModelForm, widgets

class AddAsignacionCursoEstudiante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['asignacionCurso'].widget.attrs['autofocus'] = True
    class Meta:
        model = AsignacionCursoEstudiante
        fields = '__all__'
        
