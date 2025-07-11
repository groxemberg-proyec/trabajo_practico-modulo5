from django.urls import path
from . import views

app_name = 'calificaciones'

urlpatterns = [
    path('registrar/', views.registrar_calificacion, name='registrar'),
    path('lista/', views.lista_calificaciones, name='lista'),
]
