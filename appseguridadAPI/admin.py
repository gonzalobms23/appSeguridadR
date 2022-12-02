from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from appseguridadAPI.models import *
# Register your models here.
class UsuarioAdmin(admin.ModelAdmin):
    fields = [
        "username","email","first_name", "last_name",
        "codigo","area","cargo","nombre","apellidos","turnos","estado","date_joined"
    ]


admin.site.register(Area)
admin.site.register(Cargo)
admin.site.register(AdminUser,UserAdmin)
admin.site.register(Usuario,UsuarioAdmin)
admin.site.register(Sesiones)
admin.site.register(Peligro)
admin.site.register(Riesgo)
admin.site.register(Procesos)
admin.site.register(Reporte)
admin.site.register(SolicitudCreacion)
admin.site.register(Urgencia)