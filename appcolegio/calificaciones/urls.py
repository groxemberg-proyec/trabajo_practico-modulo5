from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'gestiones', views.GestionViewSet)
router.register(r'periodos', views.PeriodoViewSet)
router.register(r'asignaturas', views.AsignaturaViewSet)
router.register(r'calificaciones', views.CalificacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

