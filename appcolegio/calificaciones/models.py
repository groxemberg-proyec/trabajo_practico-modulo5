from django.db import models
from personas.models import Profesor, Estudiante
from .validators import validar_calificacion

# GESTIÓN

class Gestion(models.Model):
    nombre_gestion = models.CharField(max_length=10, unique=True)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_gestion
    
    class Meta:
        verbose_name = "Gestión"
        verbose_name_plural = "Gestiones"

# PERÍODO

class Periodo(models.Model):
    gestion = models.ForeignKey(Gestion, on_delete=models.CASCADE, related_name="periodos")
    nombre_periodo = models.CharField(max_length=45)
    posicion_ordinal = models.PositiveSmallIntegerField()
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombre_periodo} - {self.gestion}"

# ASIGNATURA

class Asignatura(models.Model):
    profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE)
    nombre_asignatura = models.CharField(max_length=45)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_asignatura

# CALIFICACIÓN

class Calificacion(models.Model):
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    asignatura = models.ForeignKey(Asignatura, on_delete=models.CASCADE)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)

    calificacion_general = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validar_calificacion])
    calificacion_actitudes = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validar_calificacion])          # antes: calificacion_ser
    calificacion_conocimiento = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validar_calificacion])       # antes: calificacion_saber
    calificacion_practica = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validar_calificacion])           # antes: calificacion_hacer
    calificacion_pensamiento_critico = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validar_calificacion])# antes: calificacion_decidir
    calificacion_autoevaluacion = models.PositiveSmallIntegerField(null=True, blank=True, validators=[validar_calificacion])

    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Estudiante {self.estudiante} - {self.asignatura.nombre_asignatura} - {self.periodo.nombre_periodo}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"