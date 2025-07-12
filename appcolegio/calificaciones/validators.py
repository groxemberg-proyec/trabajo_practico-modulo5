from django.core.exceptions import ValidationError

def validar_calificacion(value):
    if value is not None and (value < 0 or value > 100):
        raise ValidationError('La calificación debe estar entre 0 y 100.')
