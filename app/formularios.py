from app.models import Asistencia
from django.forms import ModelForm, fields

class AddAsistenciaForm(ModelForm):
    class Meta:
        model = Asistencia
        fields = '__all__'
