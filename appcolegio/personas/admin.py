from django.contrib import admin
from .models import Colegio, Persona, Profesor, Estudiante

@admin.display(description='Nombre(s)')
def nombre_persona(obj):
    return obj.persona.nombres

@admin.display(description='Apellido(s)')
def apellido_persona(obj):
    return f"{obj.persona.apellido_paterno} {obj.persona.apellido_materno}"

class ColegioAdmin(admin.ModelAdmin):
    list_display = ('nombre_colegio', 'direccion', 'telefono', 'sitio_web')
    search_fields = ('nombre_colegio',)
    list_filter = ('estado',)
    ordering = ('nombre_colegio',)

class PersonaAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido_paterno', 'apellido_materno', 'cedula_identidad_numero')
    search_fields = ('nombres', 'apellido_paterno', 'apellido_materno')
    list_filter = ('estado',)
    ordering = ('nombres',)



class ProfesorAdmin(admin.ModelAdmin):
    list_display = (nombre_persona, apellido_persona, 'estado')
    search_fields = ('persona__nombres', 'persona__apellido_paterno', 'persona__apellido_materno')
    list_filter = ('estado',)
    ordering = ('persona__nombres',)



class EstudianteAdmin(admin.ModelAdmin):
    list_display = (nombre_persona, apellido_persona, 'curso', 'salud_alergias', 'salud_grupo_sanguineo')
    search_fields = ('persona__nombres', 'persona__apellido_paterno', 'persona__apellido_materno')
    list_filter = ('curso', 'salud_grupo_sanguineo')
    ordering = ('persona__nombres',)

admin.site.register(Colegio, ColegioAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Estudiante, EstudianteAdmin)

