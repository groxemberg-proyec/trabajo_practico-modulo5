

# Create your views here.
from django.shortcuts import render, redirect
from .models import Calificacion, Asignatura, Periodo
from .forms import CalificacionForm

def registrar_calificacion(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('calificaciones:lista')
    else:
        form = CalificacionForm()
    
    return render(request, 'calificaciones/registrar_calificacion.html', {'form': form})

def lista_calificaciones(request):
    calificaciones = Calificacion.objects.select_related('asignatura', 'periodo').all()
    return render(request, 'calificaciones/lista_calificaciones.html', {'calificaciones': calificaciones})
