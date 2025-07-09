from django.db import models
from .validators import validar_alfabetico, validar_entero_positivo, validar_longitud_minima, validar_un_solo_caracter

# NIVEL

class Nivel(models.Model):
    nombreNivel = models.CharField(max_length=20, validators=[validar_alfabetico,validar_longitud_minima,]) # 'Primaria', 'Secundaria', etc.
    posicion_ordinal = models.PositiveIntegerField(default=1, validators=[validar_entero_positivo,]) # Posición en el orden de los niveles, 1,2 etc.
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreNivel


# GRADO

class Grado(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE) # Relación con Nivel
    nombreGrado = models.CharField(max_length=100, validators=[validar_alfabetico,]) # 'Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto', etc.
    posicion_ordinal = models.PositiveIntegerField(default=1, validators=[validar_entero_positivo,]) # Posición en el orden de los grados, 1,2,3,4,5,6 etc.
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombreGrado} - {self.nivel.nombreNivel}"


# PARALELO

class Paralelo(models.Model):
    nombreParalelo = models.CharField(max_length=1, validators=[validar_alfabetico, validar_un_solo_caracter,])  # 'A', 'B', etc.
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreParalelo


# CURSO

class Curso(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE) # Relación con Grado
    paralelo = models.ForeignKey(Paralelo, on_delete=models.CASCADE) # Relación con Paralelo
    nombreCurso = models.CharField(max_length=100, validators=[validar_longitud_minima,]) # 'Primero de Primaria A' | '1PA', 'Primero de Primaria B' | '1PB', 'Segundo de Secundaria A' | '2SA', 'Segundo de Secundaria B' | '2SB', etc.
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombreCurso} ({self.grado} {self.paralelo})"