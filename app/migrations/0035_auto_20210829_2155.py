# Generated by Django 3.1.3 on 2021-08-30 02:55

import app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0034_auto_20210829_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talento_humano',
            name='CopiaCedula',
            field=models.FileField(upload_to=app.models.CopiadeCedula),
        ),
    ]
