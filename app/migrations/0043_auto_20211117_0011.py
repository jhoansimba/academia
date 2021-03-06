# Generated by Django 3.1.3 on 2021-11-17 05:11

import app.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0042_asistencia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='comprobante',
            name='nivel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.numero'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='Antecedentes',
            field=models.FileField(upload_to=app.models.CertificadoAntecedentes, verbose_name='4. Certificado Antecedentes Penales'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='CarnetDiscap',
            field=models.FileField(upload_to=app.models.CarnetDiscapacidad, verbose_name='9. Copia de carnet de discapcidad '),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='CertiBancaria',
            field=models.FileField(upload_to=app.models.CertificacionBancaria, verbose_name='10. Certificación Bancaria de la institucion financiera que corresponda'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='CertiImpedimento',
            field=models.FileField(upload_to=app.models.CertificadoNoImpedimento, verbose_name='3. Certificado de no tener impedimento de trabajo'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='CopiaCedula',
            field=models.FileField(upload_to=app.models.CopiadeCedula, verbose_name='2. Copia de la cédula'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='CopiaRuc',
            field=models.FileField(upload_to=app.models.Ruc, verbose_name='11. Copia de RUC'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='Cursos',
            field=models.FileField(upload_to=app.models.CertificadosCapacitacion, verbose_name='7. Certificados de eventos de capacitación en los ultimos 5 años'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='Experiencia',
            field=models.FileField(upload_to=app.models.ExperienciaLaboral, verbose_name='6. Certificados de experiencia laboral'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='Historial',
            field=models.FileField(upload_to=app.models.HistorialLaboral, verbose_name='8. Impresión de historial Laboral '),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='HojaVida',
            field=models.FileField(upload_to=app.models.HojaDeVida, verbose_name='1. Hoja de Vida'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='Titulos',
            field=models.FileField(upload_to=app.models.TitulosAcreditados, verbose_name='5. Título que acredite su profesión'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='cedula_th',
            field=models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Cédula'),
        ),
        migrations.AlterField(
            model_name='talento_humano',
            name='imagen_th',
            field=models.ImageField(null=True, upload_to='images/talento_humano', verbose_name='Fotografía'),
        ),
    ]
