# Generated by Django 3.1.3 on 2021-08-25 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20210825_1132'),
    ]

    operations = [
        migrations.AddField(
            model_name='talento_humano',
            name='hojaVida',
            field=models.FileField(default=1, upload_to='file/talento_humano/{{cedula_th}}/hoja de vida'),
            preserve_default=False,
        ),
    ]