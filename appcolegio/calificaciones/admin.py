from django.contrib import admin
from .models import Gestion, Periodo, Asignatura, Calificacion

from personas.models import Profesor, Estudiante

# MODELOS
@admin.register(Gestion)
class GestionAdmin(admin.ModelAdmin):
    list_display = ('nombre_gestion', 'estado', 'fecha_registro')
    list_filter = ('estado',)
    search_fields = ('nombre_gestion',)


@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ('nombre_periodo', 'gestion', 'posicion_ordinal', 'estado')
    list_filter = ('gestion', 'estado')
    search_fields = ('nombre_periodo',)


@admin.register(Asignatura)
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre_asignatura', 'profesor', 'estado')
    list_filter = ('estado', 'profesor')
    search_fields = ('nombre_asignatura',)


@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = (
        'estudiante', 'asignatura', 'periodo',
        'calificacion_general',
        'calificacion_actitudes',
        'calificacion_conocimiento',
        'calificacion_practica',
        'calificacion_pensamiento_critico',
        'calificacion_autoevaluacion',
        'estado'
    )
    list_filter = ('periodo', 'asignatura', 'estado')
    search_fields = ('estudiante__persona__nombres', 'asignatura__nombre_asignatura')

