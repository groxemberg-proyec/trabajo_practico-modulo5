from django.db import models
from personas.models import Profesor, Estudiante

# GESTIÓN

class Gestion(models.Model):
    nombre_gestion = models.CharField(max_length=10, unique=True)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombre_gestion

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

    calificacion_general = models.PositiveSmallIntegerField(null=True, blank=True)
    calificacion_ser = models.PositiveSmallIntegerField(null=True, blank=True)
    calificacion_saber = models.PositiveSmallIntegerField(null=True, blank=True)
    calificacion_hacer = models.PositiveSmallIntegerField(null=True, blank=True)
    calificacion_decidir = models.PositiveSmallIntegerField(null=True, blank=True)
    calificacion_autoevaluacion = models.PositiveSmallIntegerField(null=True, blank=True)

    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Estudiante {self.estudiante} - {self.asignatura.nombre_asignatura} - {self.periodo.nombre_periodo}"
