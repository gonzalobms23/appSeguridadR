# Generated by Django 4.1.3 on 2022-11-27 04:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appseguridadAPI', '0002_procesos_riesgo_alter_usuario_turnos_sesiones_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='peligro',
            name='sesion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='peligro', to='appseguridadAPI.sesiones'),
        ),
        migrations.RemoveField(
            model_name='sesiones',
            name='Usuario',
        ),
        migrations.AddField(
            model_name='sesiones',
            name='Usuario',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]