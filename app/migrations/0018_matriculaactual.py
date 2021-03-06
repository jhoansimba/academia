# Generated by Django 3.1.3 on 2021-08-21 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20210818_2114'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatriculaActual',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inicio', models.DateField(verbose_name='Inicio del Período académico')),
                ('fin', models.DateField(verbose_name='Fin del Período académico')),
                ('estudiante', models.ManyToManyField(to='app.Estudiante')),
            ],
        ),
    ]
