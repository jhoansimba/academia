# Generated by Django 3.1.3 on 2021-11-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20210912_2330'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='categoria',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
