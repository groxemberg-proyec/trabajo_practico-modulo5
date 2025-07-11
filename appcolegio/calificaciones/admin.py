from django.contrib import admin
from .models import Gestion, Periodo, Asignatura, Calificacion
from personas.models import Profesor, Estudiante  # Cambia 'tuapp' por el nombre correcto de tu app

# MODELOS LOCALES

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
        'calificacion_general', 'calificacion_ser',
        'calificacion_saber', 'calificacion_hacer',
        'calificacion_decidir', 'calificacion_autoevaluacion',
        'estado'
    )
    list_filter = ('periodo', 'asignatura', 'estado')
    search_fields = ('estudiante__persona__nombres', 'asignatura__nombre_asignatura')


# OPCIONAL: Registrar Profesor y Estudiante si no están en otro admin.py

@admin.register(Profesor)
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ('persona', 'numero_celular', 'estado')
    search_fields = ('persona__nombres', 'persona__apellido_paterno')


@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('persona', 'curso', 'estado')
    search_fields = ('persona__nombres', 'persona__apellido_paterno')

