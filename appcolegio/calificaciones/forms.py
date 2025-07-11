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
            'calificacion_ser',
            'calificacion_saber',
            'calificacion_hacer',
            'calificacion_decidir',
            'calificacion_autoevaluacion',
        ]
