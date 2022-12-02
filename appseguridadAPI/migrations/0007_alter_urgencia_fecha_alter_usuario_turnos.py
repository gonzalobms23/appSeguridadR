# Generated by Django 4.1.3 on 2022-12-01 06:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appseguridadAPI', '0006_alter_usuario_turnos_urgencia'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urgencia',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='fecha'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='turnos',
            field=models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')], default='M', max_length=20, verbose_name='Turnos'),
        ),
    ]
