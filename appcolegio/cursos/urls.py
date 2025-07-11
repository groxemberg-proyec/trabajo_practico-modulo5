from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'cursos', views.CursoViewSet)
router.register(r'grados', views.GradoViewSet)
router.register(r'paralelos', views.ParaleloViewSet)
router.register(r'niveles', views.NivelViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('cursos-activos/', views.cursos_activos),
]