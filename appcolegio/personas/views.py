from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .models import Colegio, Persona, Estudiante, Profesor
from .serializers import ColegioSerializer, PersonaSerializer, EstudianteSerializer, ProfesorSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response

class ColegioViewSet(viewsets.ModelViewSet):
    queryset = Colegio.objects.all()
    serializer_class = ColegioSerializer
  

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
 
class EstudianteViewSet(viewsets.ModelViewSet):
    queryset = Estudiante.objects.all()
    serializer_class = EstudianteSerializer

class ProfesorViewSet(viewsets.ModelViewSet):
    queryset = Profesor.objects.all()
    serializer_class = ProfesorSerializer


def estudiantes(request):
    return HttpResponse("Listado de estudiantes")

@api_view(['GET'])
def estudiantes_activo(request):
    estudiantes = Estudiante.objects.filter(estado=True)
    serializer = EstudianteSerializer(estudiantes, many=True)
    return Response(serializer.data)
