# Generated by Django 3.1.3 on 2021-08-09 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_cursos_imagen_curso'),
        ('User', '0004_usuario_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Programa',
            field=models.ManyToManyField(blank=True, to='app.Programa'),
        ),
    ]
