# Generated by Django 3.1.3 on 2021-09-13 00:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0039_auto_20210831_2223'),
        ('User', '0014_paralelo_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paralelo',
            name='nivel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.numero'),
        ),
        migrations.DeleteModel(
            name='NivelesGenerales',
        ),
    ]
