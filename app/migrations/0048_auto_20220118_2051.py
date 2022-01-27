# Generated by Django 3.1.3 on 2022-01-19 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0047_auto_20220112_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='email_est',
            field=models.EmailField(max_length=254, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='id_direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.direccion', verbose_name='Dirección Domiciliaria'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='telefono_est',
            field=models.CharField(max_length=10, verbose_name='Número de Telefono'),
        ),
        migrations.AlterField(
            model_name='ficha_salud',
            name='telefonoEmer_fichsal',
            field=models.CharField(max_length=10, verbose_name='Teléfono de emergencia'),
        ),
        migrations.AlterField(
            model_name='matriculaactual',
            name='nivel',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.numero'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='telefono',
            field=models.CharField(max_length=10, verbose_name='Teléfono'),
        ),
    ]
