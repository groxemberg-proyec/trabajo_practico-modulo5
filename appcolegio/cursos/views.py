from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Curso, Grado, Paralelo, Nivel
from .serializers import CursoSerializer, GradoSerializer, ParaleloSerializer, NivelSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class GradoViewSet(viewsets.ModelViewSet):
    queryset = Grado.objects.all()
    serializer_class = GradoSerializer

class ParaleloViewSet(viewsets.ModelViewSet):
    queryset = Paralelo.objects.all()
    serializer_class = ParaleloSerializer

class NivelViewSet(viewsets.ModelViewSet):
    queryset = Nivel.objects.all()
    serializer_class = NivelSerializer

# Create your views here.
def cursos(request):
    return HttpResponse("Listado de cursos")

