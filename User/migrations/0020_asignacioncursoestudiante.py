# Generated by Django 3.1.3 on 2021-11-08 01:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20210912_2330'),
        ('User', '0019_asignacioncurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionCursoEstudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asignacionCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.asignacioncurso')),
                ('estudiantes', models.ManyToManyField(to='app.Estudiante')),
            ],
        ),
    ]