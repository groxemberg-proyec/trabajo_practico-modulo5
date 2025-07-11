from  django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

# RUTAS PARA API REST VIEWSETS
# Usamos DefaultRouter para registrar los viewsets y generar automáticamente las rutas
router = DefaultRouter()
router.register(r'colegios', views.ColegioViewSet)
router.register(r'personas', views.PersonaViewSet)
router.register(r'estudiantes', views.EstudianteViewSet)
router.register(r'profesores', views.ProfesorViewSet)

urlpatterns = [
    #path('personas', views.personas, name='personas'),
    #path('', views.index, name='index'), 

    # Incluir las rutas generadas por el router
    path('', include(router.urls)),
    path('estudiantes-activos/', views.estudiantes_activo),
]