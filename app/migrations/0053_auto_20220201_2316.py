# Generated by Django 3.1.3 on 2022-02-02 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0052_asistencia_programaid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='programaID',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
