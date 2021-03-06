# Generated by Django 3.1.3 on 2021-11-08 01:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20210912_2330'),
        ('User', '0018_auto_20210912_2226'),
    ]

    operations = [
        migrations.CreateModel(
            name='AsignacionCurso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('curso', models.ManyToManyField(to='app.Cursos')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
