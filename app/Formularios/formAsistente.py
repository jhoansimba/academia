from User.models import AsigacionParalelo, Paralelo, Periodo, ProgramaGeneral
from django.forms import ModelForm, widgets
from django import forms
from app.models import Cursos, Ficha_salud, Horarios, Matricula, Programa, Talento_Humano
from django.forms import ModelForm, widgets


class FormMatricula(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['fecha'].widget.attrs['autofocus'] = True
        self.fields['matricula'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Matricula
        fields = '__all__'


class EditMatricula(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        self.fields['matricula'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Matricula
        fields = '__all__'
        exclude = 'estudiante', ''


class FormHorarios(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
      #  self.fields['fecha'].widget.attrs['autofocus'] = True
       # self.fields['matricula'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Programa
        fields = '__all__'


class FormHorarios2(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
      #  self.fields['fecha'].widget.attrs['autofocus'] = True
       # self.fields['matricula'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Cursos
        fields = '__all__'


class EditHorarios(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
       # self.fields['matricula'].widget.attrs['class'] = 'form-check-input'

    class Meta:
        model = Cursos
        fields = '__all__'


class FormHumano (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
            self.fields['cedula_th'].widget.attrs['onkeypress'] = "return soloNumeros(event)"
            self.fields['telefono'].widget.attrs['onkeypress'] = "return soloNumeros(event)"

    class Meta:
        model = Talento_Humano
        fields = '__all__'


class AgregarEstudiantesForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
        # self.fields['id_est'].widget.attrs['autofocus'] = True
        # self.fields['id_direccion'].widget.attrs['class'] = 'custom-select'

    class Meta:
        model = AsigacionParalelo
        fields = '__all__'


class FormPeriodo (ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'

    class Meta:
        model = Periodo
        fields = '__all__'
        
class FormParalelo(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
            # self.fields['id_est'].widget.attrs['autofocus'] = True
             # self.fields['id_direccion'].widget.attrs['class'] = 'custom-select'

    class Meta:
        model = Paralelo
        fields = '__all__'
class FormProgramaGeneral(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for i in self.visible_fields():
            i.field.widget.attrs['class'] = 'form-control'
            i.field.widget.attrs['autocomplete'] = 'off'
            # self.fields['id_est'].widget.attrs['autofocus'] = True
             # self.fields['id_direccion'].widget.attrs['class'] = 'custom-select'

    class Meta:
        model = ProgramaGeneral
        fields = '__all__'
