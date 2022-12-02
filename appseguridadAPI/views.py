from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import *
# Create your views here.

class AreaList(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class AreaDetail(generics.RetrieveAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer

class CargoList(generics.ListCreateAPIView):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer

class SesionesList(generics.ListCreateAPIView):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer

class SesionesDetail(generics.RetrieveAPIView):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer

class SesionesDetailUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer

class SesionesListUser(generics.ListAPIView):
    queryset = Sesiones.objects.all()
    serializer_class = SesionesSerializer

    def get_queryset(self):
        id=self.kwargs['pk']
        user=Usuario.objects.get(pk=id)
        sesion=Sesiones.objects.filter(Usuario=user)
        return sesion



class SolicitudCreacion(generics.CreateAPIView):
    queryset = SolicitudCreacion.objects.all()
    serializer_class = SolicitudSerializer

class UsuariosList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class UsuariosDetail(generics.RetrieveAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class PeligrosSesionList(generics.ListCreateAPIView):
    queryset = Peligro.objects.all()
    serializer_class = PeligroSerializer

    def get_queryset(self):
        id=self.kwargs['pk']
        sesion=Sesiones.objects.get(pk=id)
        peligro=Peligro.objects.filter(sesion=sesion)
        return peligro

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class ReporteListCreate(generics.ListCreateAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

class ReporteUser(generics.ListAPIView):
    queryset = Reporte.objects.all()
    serializer_class = ReporteSerializer

    def get_queryset(self):
        id=self.kwargs['pk']
        user=Usuario.objects.get(pk=id)
        reporte=Reporte.objects.filter(Usuario=user)
        return reporte

class UrgenciaListCreate(generics.ListCreateAPIView):
    queryset = Urgencia.objects.all()
    serializer_class = UrgenciaSerializer

class PeligroListCreate(generics.ListCreateAPIView):
    queryset = Peligro.objects.all()
    serializer_class = PeligroSerializer

class RiesgoListCreate(generics.ListCreateAPIView):
    queryset = Riesgo.objects.all()
    serializer_class = RiesgoSerializer

class ProcesoListCreate(generics.ListCreateAPIView):
    queryset = Procesos.objects.all()
    serializer_class = ProcesosSerializer

class PeligroListCreateNested(generics.ListCreateAPIView):
    queryset = Peligro.objects.all()
    serializer_class = PeligroCreateNestedSerializer