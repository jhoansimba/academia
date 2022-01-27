from django import forms
from app.models import Comprobante, Estudiante
from django.forms import ModelForm, widgets

class AddEstudiante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['id_est'].widget.attrs['autofocus'] = True
        self.fields['id_direccion'].widget.attrs['class'] = 'custom-select'
        self.fields['id_est'].widget.attrs['onkeypress'] = "return soloNumeros(event)"
        self.fields['telefono_est'].widget.attrs['onkeypress'] = "return soloNumeros(event)"
    class Meta:
        model = Estudiante
        fields = '__all__'
        
class FormEstudiante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['id_est'].widget.attrs['readonly'] = True
        # self.fields['fecha_est'].widget.attrs['hidden'] = True
    class Meta:
        model = Estudiante
        fields = '__all__'
        exclude = ('fecha_est','id_rep')

class AddComprobante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['id_est'].widget.attrs['autofocus'] = True
      
    class Meta:
        model = Comprobante
        fields = '__all__'

class FormComprobante(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['id_est'].widget.attrs['disabled'] = True
        # self.fields['fecha_est'].widget.attrs['hidden'] = True
    class Meta:
        model = Comprobante
        fields = '__all__'
        exclude = ('id_est','')