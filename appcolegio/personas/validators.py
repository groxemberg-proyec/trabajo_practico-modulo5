from django.core.exceptions import ValidationError
import re

#COLEGIO
def nombre_colegio(value):
    if len(value.strip()) < 3:
        raise ValidationError("El nombre del colegio debe tener al menos 3 caracteres.")

#PERSONA
def cedula(value   ):
    if len(value) < 6 or len(value) > 10:
        raise ValidationError("La cédula debe tener entre 6 y 9 dígitos.")

#PRFESOR

def celular(value):
    if not re.fullmatch(r'\d{8,15}', value):
        raise ValidationError("El número de celular debe tener entre 8 y 15 dígitos numéricos.")

#ESTUDIANTE

def grupo_sanguineo(value):
    grupos_validos = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
    if value.upper() not in grupos_validos:
        raise ValidationError("Grupo sanguíneo inválido. Use por ejemplo: A+, O-, etc.")