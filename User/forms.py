from User.models import Usuario
from django.db import models
from django.forms import ModelForm, fields, widgets
from django.contrib.auth.models import AbstractUser, User
class FormularioUser(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['username'].widget.attrs['autofocus'] = True
        # self.fields['password'].widget.attrs['hidden'] = True
        # self.fields['is_superuser'].widget.attrs['class'] = 'form-check-input'
        self.fields['is_staff'].widget.attrs['class'] = 'form-check-input'
        self.fields['curso'].widget.attrs['hidden'] = True
        self.fields['programa'].widget.attrs['hidden'] = True
    class Meta:
        model = Usuario
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'groups', 'is_staff', 'curso', 'programa')
        labels = {
            'username' : 'Cédula de Identidad',
            'first_name':'Nombres', 
            'is_staff':'Activo'
        }
        