from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Curso, Grado, Paralelo, Nivel
from .serializers import CursoSerializer, GradoSerializer, ParaleloSerializer, NivelSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

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

@api_view(['GET'])
def cursos_activos(request):
    cursos = Curso.objects.filter(estado=True)
    serializer = CursoSerializer(cursos, many=True)
    return Response(serializer.data)