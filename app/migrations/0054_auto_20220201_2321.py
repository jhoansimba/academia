# Generated by Django 3.1.3 on 2022-02-02 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0053_auto_20220201_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asistencia',
            name='programaID',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
