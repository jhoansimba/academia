# Generated by Django 3.1.3 on 2021-12-16 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0044_matricula_nivel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Galeria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='')),
                ('tiulo', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='apellidos_est',
            field=models.CharField(max_length=25, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='email_est',
            field=models.EmailField(max_length=254, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id_curso',
            field=models.ManyToManyField(blank=True, null=True, to='app.Cursos', verbose_name='Cursos'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id_direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.direccion', verbose_name='Direccion Domiciliaria'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id_est',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id_programa',
            field=models.ManyToManyField(blank=True, null=True, to='app.Programa', verbose_name='Programas'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='imagen_est',
            field=models.ImageField(null=True, upload_to='images/estudiante', verbose_name='Fotografía'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='nombres_est',
            field=models.CharField(max_length=25, verbose_name='Nombres'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='telefono_est',
            field=models.CharField(max_length=10, verbose_name='Numero de Telefono'),
        ),
    ]
