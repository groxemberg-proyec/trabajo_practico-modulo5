from django.core.exceptions import ValidationError

def validar_alfabetico(value):
    if not value.isalpha():
        raise ValidationError("El valor debe ser un texto alfabético (sin números ni caracteres especiales).")
    
def validar_entero_positivo(value):
    if not isinstance(value, int) or value < 1:
        raise ValidationError("El valor debe ser un número entero positivo.")

def validar_longitud_minima(value):
    if len(value) < 3:
        raise ValidationError("El valor debe tener al menos 3 caracteres.")
    
def validar_un_solo_caracter(value):
    if len(value) != 1:
        raise ValidationError("El valor debe ser un solo carácter alfabético.")