from django.db import models
from django.core.exceptions import ValidationError

# NIVEL

class Nivel(models.Model):
    nombreNivel = models.CharField(max_length=20) # 'Primaria', 'Secundaria', etc.
    posicion_ordinal = models.PositiveIntegerField(default=1) # Posición en el orden de los niveles, 1,2 etc.
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreNivel
    
    # Validaciones para Nivel
    def clean(self):
        if not self.nombreNivel.isalpha():
            raise ValidationError("El nivel debe ser un texto alfabético (Primaria, Secundaria, etc.).")
        if len(self.nombreNivel) < 3:
            raise ValidationError("El nombre del nivel debe tener al menos 3 caracteres.")
        if self.posicion_ordinal < 1: 
            raise ValidationError("La posición ordinal del grado debe ser un número positivo.")

# GRADO

class Grado(models.Model):
    nivel = models.ForeignKey(Nivel, on_delete=models.CASCADE) # Relación con Nivel
    nombreGrado = models.CharField(max_length=100) # 'Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto', 'Sexto', etc.
    posicion_ordinal = models.PositiveIntegerField(default=1) # Posición en el orden de los grados, 1,2,3,4,5,6 etc.
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombreGrado} - {self.nivel.nombreNivel}"

    # Validaciones para Grado
    def clean(self):
        if not self.nombreGrado.isalpha():
            raise ValidationError("El grado debe ser un texto alfabético (Primero, Segundo, Tercero, etc.).")
        if self.posicion_ordinal < 1: 
            raise ValidationError("La posición ordinal del grado debe ser un número positivo.")

# PARALELO

class Paralelo(models.Model):
    nombreParalelo = models.CharField(max_length=1)  # 'A', 'B', etc.
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nombreParalelo
    
    # Validación para Paralelo
    def clean(self):
        if not self.nombreParalelo.isalpha():
            raise ValidationError("El paralelo debe ser una letra del alfabeto (A, B, C, etc.).")

# CURSO

class Curso(models.Model):
    grado = models.ForeignKey(Grado, on_delete=models.CASCADE) # Relación con Grado
    paralelo = models.ForeignKey(Paralelo, on_delete=models.CASCADE) # Relación con Paralelo
    nombreCurso = models.CharField(max_length=100) # 'Primero de Primaria A' | '1PA', 'Primero de Primaria B' | '1PB', 'Segundo de Secundaria A' | '2SA', 'Segundo de Secundaria B' | '2SB', etc.
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nombreCurso} ({self.grado} {self.paralelo})"
    
    # Validación para Curso
    def clean(self):
        if len(self.nombreCurso) < 5:
            raise ValidationError("El nombre del curso debe tener al menos 3 caracteres.")