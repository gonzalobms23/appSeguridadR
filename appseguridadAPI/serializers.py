from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.fields import SerializerMethodField
from drf_writable_nested.serializers import WritableNestedModelSerializer

from .models import *

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        print(user.id)
        token['id'] = user.id
        return token

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cargo
        fields="__all__"

class AreaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Area
        fields="__all__"

class RiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Riesgo
        fields=['riesgo']

class ProcesosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Procesos
        fields=['nombre']

class PeligroSerializer(serializers.ModelSerializer):

    class Meta:
        model=Peligro
        fields="__all__"

class PeligroCreateNestedSerializer(WritableNestedModelSerializer):

    riesgo=RiesgoSerializer(allow_null=True)
    proceso=ProcesosSerializer(allow_null=True)
    class Meta:
        model=Peligro
        fields="__all__"


class SesionesSerializer(serializers.ModelSerializer):
    peligro=PeligroSerializer(many=True)

    class Meta:
        model=Sesiones
        fields="__all__"

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Reporte
        fields="__all__"

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Usuario
        fields="__all__"

class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model=SolicitudCreacion
        fields="__all__"

class UrgenciaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Urgencia
        fields="__all__"

