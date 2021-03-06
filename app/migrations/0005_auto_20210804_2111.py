# Generated by Django 3.1.3 on 2021-08-05 02:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cursos_detalle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='id_curso',
            field=models.ManyToManyField(blank=True, null=True, to='app.Cursos'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id_programa',
            field=models.ManyToManyField(blank=True, null=True, to='app.Programa'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='p_nota1',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Trabajos'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='p_nota2',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Tareas'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='p_nota3',
            field=models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='examen'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='s_nota1',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Trabajos'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='s_nota2',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Tareas'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='s_nota3',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='examen'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='t_nota1',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Trabajos'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='t_nota2',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='Tareas'),
        ),
        migrations.AlterField(
            model_name='notas',
            name='t_nota3',
            field=models.FloatField(blank=True, default=0, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)], verbose_name='examen'),
        ),
    ]
