# Generated by Django 3.1.3 on 2021-11-12 01:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0020_asignacioncursoestudiante'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignacioncursoestudiante',
            old_name='estudiantes',
            new_name='estudiantesCurso',
        ),
    ]