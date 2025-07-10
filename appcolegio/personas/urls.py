from   django.urls import path
from . import views

urlpatterns = [
    path('personas', views.personas, name='personas'),
    #path('', views.index, name='index'), 
]