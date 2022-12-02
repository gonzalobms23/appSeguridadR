from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from appseguridadAPI.models import *
# Register your models here.
admin.site.register(Area)
admin.site.register(Cargo)
admin.site.register(AdminUser)
admin.site.register(Usuario)
admin.site.register(Sesiones)
admin.site.register(Peligro)
admin.site.register(Riesgo)
admin.site.register(Procesos)
admin.site.register(Reporte)
admin.site.register(SolicitudCreacion)
admin.site.register(Urgencia)