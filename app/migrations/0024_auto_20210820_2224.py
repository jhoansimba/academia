# Generated by Django 3.1.3 on 2021-08-21 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_auto_20210820_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='niveles',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
