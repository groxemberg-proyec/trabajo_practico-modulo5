from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def cursos(request):
    return HttpResponse("Listado de cursos")