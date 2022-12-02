from django.urls import path
from .views import AreaList,SesionesList,CargoList,SesionesDetail,SesionesListUser,\
    SolicitudCreacion,UsuariosList,UsuariosDetail,AreaDetail,PeligrosSesionList,ReporteListCreate,ReporteUser,\
    UrgenciaListCreate,SesionesDetailUpdate,PeligroListCreate,RiesgoListCreate,ProcesoListCreate,PeligroListCreateNested

urlpatterns = [
    path('areas/',AreaList.as_view()),
    path('areas/<int:pk>/',AreaDetail.as_view()),
    path('cargos/',CargoList.as_view()),
    path('sesiones/',SesionesList.as_view()),
    path('sesiones/<int:pk>/',SesionesDetail.as_view()),
    path('sesionesUpdate/<int:pk>/',SesionesDetailUpdate.as_view()),
    path('sesionesUser/<int:pk>/',SesionesListUser.as_view()),
    path('solicitudCreacion/',SolicitudCreacion.as_view()),
    path('usuarios/',UsuariosList.as_view()),
    path('usuarios/<int:pk>/',UsuariosDetail.as_view()),
    path('peligrosSesion/<int:pk>/',PeligrosSesionList.as_view()),
    path('reporte/',ReporteListCreate.as_view()),
    path('reporteUser/<int:pk>/',ReporteUser.as_view()),
    path('urgencia/',UrgenciaListCreate.as_view()),
    path('peligro/',PeligroListCreate.as_view()),
    path('riesgo/',RiesgoListCreate.as_view()),
    path('proceso/',ProcesoListCreate.as_view()),
    path('peligroCreate/',PeligroListCreateNested.as_view()),
]