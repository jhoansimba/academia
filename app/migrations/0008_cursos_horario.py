# Generated by Django 3.1.3 on 2021-08-09 21:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_notas_materia'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='horario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.horarios'),
            preserve_default=False,
        ),
    ]
