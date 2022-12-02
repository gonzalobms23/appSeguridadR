# Generated by Django 4.1.3 on 2022-11-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appseguridadAPI', '0004_solicitudcreacion_alter_usuario_turnos'),
    ]

    operations = [
        migrations.AddField(
            model_name='reporte',
            name='usuarioJefe',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Jefe'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='turnos',
            field=models.CharField(choices=[('M', 'Mañana'), ('T', 'Tarde'), ('N', 'Noche')], default='M', max_length=20, verbose_name='Turnos'),
        ),
    ]
