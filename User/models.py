from django.contrib.auth.password_validation import password_changed
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.forms.models import model_to_dict
from django.utils import tree
from app.models import Cursos, Programa


class Usuario(AbstractUser):
    token = models.CharField(max_length=50, blank=True, null=True)
    curso = models.ManyToManyField(Cursos, blank=True, verbose_name=" " )
    programa = models.ManyToManyField(Programa, blank=True, verbose_name=" ")
    def json(self):
        txt = model_to_dict(self)
        return txt
    def save(self, *args, **kwargs):
        print('Contraseña: ' ,self.password)
        print('Contraseña: ' ,len(self.password))
        if self.pk and len(self.password) < 50:
            self.set_password(self.password)
        if self.pk is None:
            psw = '_sha256$'
            password = str(self.password)
            if password.count(psw) == 0:
                self.set_password(self.password)
        return super().save(*args, **kwargs)

