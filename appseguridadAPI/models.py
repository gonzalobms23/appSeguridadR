from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser
from appseguridadAPI.turnos import turnos

# Create your models here.
class Area(models.Model):
    area=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.area

class Cargo(models.Model):
    cargo=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.cargo

class Usuario(AbstractUser):
    nombre=models.CharField(max_length=20,blank=True, null=True)
    apellidos=models.CharField(max_length=200,blank=True, null=True)
    codigo=models.CharField(max_length=20,blank=True, null=True)
    turnos=models.CharField(max_length=20,choices=turnos,default='M',verbose_name='Turnos')
    area=models.ForeignKey(Area,on_delete=models.CASCADE,null=True,blank=True)
    cargo=models.ForeignKey(Cargo,on_delete=models.CASCADE,null=True,blank=True)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        ordering=['id']

class AdminUser(Usuario):
    class Meta:
        proxy = True


class Sesiones(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nombre')
    Usuario = models.ManyToManyField(Usuario, null=True, blank=True)
    fecha = models.DateField(default=datetime.now,verbose_name='fecha')
    Area = models.ForeignKey(Area, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre

class Riesgo(models.Model):
    riesgo = models.TextField(null=True, blank=True, verbose_name='Riesgo')

    def __str__(self):
        return self.riesgo

class Procesos(models.Model):
    nombre=models.CharField(max_length=200,null=True,blank=True,verbose_name='Proceso')
    descripcion=models.TextField(null=True,blank=True)

    def __str__(self):
        return self.nombre

class Peligro(models.Model):
    peligro = models.TextField(null=True, blank=True, verbose_name='Peligro')
    medida_preventiva = models.TextField(null=True, blank=True, verbose_name='medida')
    riesgo = models.ForeignKey(Riesgo, on_delete=models.CASCADE, null=True, blank=True)
    proceso = models.ForeignKey(Procesos, on_delete=models.CASCADE, null=True, blank=True)
    puntaje= models.IntegerField(default=0, verbose_name='puntaje',blank=True,null=True)
    puntajeFinal= models.IntegerField(default=0, verbose_name='puntaje',blank=True,null=True)
    sesion = models.ForeignKey(Sesiones, on_delete=models.CASCADE, null=True, blank=True,related_name="peligro")

    def __str__(self):
        return self.peligro


class Reporte(models.Model):
    Usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True,blank=True)
    usuarioJefe = models.CharField(max_length=200, null=True, blank=True, verbose_name='Jefe')
    Area=models.ForeignKey(Area,on_delete=models.CASCADE,null=True,blank=True)
    descripcion=models.TextField(null=True,blank=True)

class SolicitudCreacion(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True, verbose_name='Nombre')
    apellido = models.CharField(max_length=200, null=True, blank=True, verbose_name='Apellido')
    jefe = models.CharField(max_length=200, null=True, blank=True, verbose_name='Jefe')

    def __str__(self):
        return self.jefe

class Urgencia(models.Model):

    usuario=models.ForeignKey(Usuario,on_delete=models.CASCADE,null=True,blank=True,verbose_name="usuario")
    fecha = models.DateTimeField(default=datetime.now,verbose_name='fecha')
    session=models.ForeignKey(Sesiones,on_delete=models.CASCADE,null=True,blank=True,verbose_name="session")
