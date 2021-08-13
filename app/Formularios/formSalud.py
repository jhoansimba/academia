from django.forms import ModelForm, widgets
from django import forms
from app.models import Ficha_salud
from django.forms import ModelForm, widgets

class AddSalud(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['NomEnfer_fichsa'].widget.attrs['autofocus'] = True
        
    class Meta:
        model = Ficha_salud
        fields = '__all__'
        widgets = {
            'descripcion_fichsal' : widgets.Textarea(attrs={'class':'form-control'})}


class FormSalud(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['id_est'].widget.attrs['disabled'] = True
        # self.fields['fecha_est'].widget.attrs['hidden'] = True
    class Meta:
        model = Ficha_salud
        fields = '__all__'
        exclude = ('id_est','')