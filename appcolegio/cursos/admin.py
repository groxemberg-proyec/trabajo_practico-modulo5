from django.contrib import admin
from .models import Nivel, Grado, Paralelo, Curso

class NivelAdmin(admin.ModelAdmin):
    list_display = ('nombreNivel', 'posicion_ordinal',)
    search_fields = ('nombreNivel',)
    list_filter = ('nombreNivel','posicion_ordinal',)
    ordering = ('posicion_ordinal',)

class GradoAdmin(admin.ModelAdmin):
    list_display = ('nombreGrado', 'nivel', 'posicion_ordinal',)
    search_fields = ('nombreGrado', 'nivel__nombreNivel',)
    list_filter = ('nivel', 'posicion_ordinal',)
    ordering = ('nivel__posicion_ordinal', 'posicion_ordinal',)

class ParaleloAdmin(admin.ModelAdmin):
    list_display = ('nombreParalelo',)
    search_fields = ('nombreParalelo',)
    list_filter = ('nombreParalelo',)
    ordering = ('nombreParalelo',)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nombreCurso', 'grado', 'paralelo',)
    search_fields = ('nombreCurso', 'grado__nombreGrado', 'paralelo__nombreParalelo',)
    list_filter = ('grado', 'paralelo',)
    ordering = ('grado__posicion_ordinal', 'paralelo__nombreParalelo','nombreCurso',)

admin.site.register(Nivel, NivelAdmin)
admin.site.register(Grado, GradoAdmin)
admin.site.register(Paralelo, ParaleloAdmin)
admin.site.register(Curso, CursoAdmin)
