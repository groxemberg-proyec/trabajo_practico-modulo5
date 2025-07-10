from django.db import models
from cursos.models import Curso
from personas.validators import nombre_colegio, cedula, celular, grupo_sanguineo

# COLEGIO

class Colegio(models.Model):
    nombre_colegio = models.CharField(max_length=45, validators=[nombre_colegio])
    direccion = models.CharField(max_length=180)
    telefono = models.CharField(max_length=15)
    sitio_web = models.CharField(max_length=45)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.nombre_colegio

# PERSONA

class tipoPerfil(models.TextChoices):
    SOCIO = 'ESTUDIANTES', 'Estudiantes'
    DOCENTE = 'DOCENTE', 'Docente'

class Persona(models.Model):
    colegio = models.ForeignKey(Colegio, on_delete=models.CASCADE, related_name='personas')
    nombres = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=45)
    apellido_materno = models.CharField(max_length=45)
    cedula_identidad_numero = models.CharField(max_length=9,validators=[cedula])
    cedula_identidad_expedido = models.CharField(max_length=20)
    tipo_perfil = models.CharField(
        max_length=45, 
        choices=tipoPerfil.choices,
        default=tipoPerfil.SOCIO
    )
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nombres} {self.apellido_paterno} {self.apellido_materno}'
    
# PROFESOR

class Profesor(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    numero_celular = models.CharField(max_length=15,validators=[celular])
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.persona)

# ESTUDIANTE

class Estudiante(models.Model):
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE) 
    salud_alergias = models.CharField(max_length=200)
    salud_grupo_sanguineo = models.CharField(max_length=3,validators=[grupo_sanguineo])
    salud_datos_medicos_importantes = models.CharField(max_length=200)
    estado = models.BooleanField(default=True)
    fecha_registro = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.persona)