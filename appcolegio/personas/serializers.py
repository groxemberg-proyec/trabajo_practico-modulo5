from rest_framework import serializers
from .models import Colegio, Persona, Estudiante, Profesor

class ColegioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Colegio
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
    colegio = ColegioSerializer(read_only=True)
    class Meta:
        model = Estudiante
        fields = '__all__'
        read_only_fields = ('colegio',)

class ProfesorSerializer(serializers.ModelSerializer):
    colegio = ColegioSerializer(read_only=True)
    class Meta:
        model = Profesor
        fields = '__all__'
        read_only_fields = ('colegio',)