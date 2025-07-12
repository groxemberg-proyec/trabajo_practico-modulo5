from django import forms
from .models import Calificacion

class CalificacionForm(forms.ModelForm):
    class Meta:
        model = Calificacion
        fields = [
            'periodo',
            'asignatura',
            'id_estudiante',
            'calificacion_general',
            'calificacion_actitudes',   
            'calificacion_conocimiento',
            'calificacion_practica',        
            'calificacion_pensamiento_critico',
            'calificacion_autoevaluacion',
        ]

