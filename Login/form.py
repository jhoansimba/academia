from django.db import models
from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import EmailInput, TextInput
# Create your models here.
class resetPasswordForm(forms.Form):
    username = forms.CharField(
        widget=TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el usuario a reestablecer',
            'autocomplete' : 'off'
            }),label='Usuario'
    )
    email = forms.EmailField(
        widget=EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Ingrese el email de este usuario',
            'autocomplete' : 'off'
            }),label='Email'
    )
    
