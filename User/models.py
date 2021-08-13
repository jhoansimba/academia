from django.contrib.auth.password_validation import password_changed
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import CASCADE
from django.utils import tree
from app.models import Cursos, Programa


class Usuario(AbstractUser):
    token = models.CharField(max_length=50, blank=True, null=True)
    curso = models.ManyToManyField(Cursos, blank=True)
    Programa = models.ManyToManyField(Programa, blank=True)
    def save(self, *args, **kwargs):
        if self.pk and len(self.password) != 88:
                self.set_password(self.password)
        if self.pk is None:
                pw = str(self.password)
                cont = '_sha256$'
                if pw.count(cont) == 0:
                        self.set_password(self.password)
        return super().save(*args, **kwargs)

