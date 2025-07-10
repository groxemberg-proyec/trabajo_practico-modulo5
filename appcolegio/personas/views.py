from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def personas(request):
    return HttpResponse("Listado de personas")
    