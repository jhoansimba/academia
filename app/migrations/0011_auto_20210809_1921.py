# Generated by Django 3.1.3 on 2021-08-10 00:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_programa_horario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='programa',
            old_name='horario',
            new_name='horario_pro',
        ),
        migrations.RenameField(
            model_name='programa',
            old_name='imagen',
            new_name='imagen_pro',
        ),
        migrations.RenameField(
            model_name='programa',
            old_name='nombre',
            new_name='nombre_pro',
        ),
    ]
