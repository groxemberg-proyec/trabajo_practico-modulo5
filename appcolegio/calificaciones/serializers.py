from rest_framework import serializers
from .models import Gestion, Periodo, Asignatura, Calificacion
from personas.serializers import EstudianteSerializer, ProfesorSerializer

class GestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gestion
        fields = '__all__'

class PeriodoSerializer(serializers.ModelSerializer):
    gestion = GestionSerializer(read_only=True)

    class Meta:
        model = Periodo
        fields = '__all__'

class AsignaturaSerializer(serializers.ModelSerializer):
    profesor = ProfesorSerializer(read_only=True)

    class Meta:
        model = Asignatura
        fields = '__all__'

class CalificacionSerializer(serializers.ModelSerializer):
    estudiante = EstudianteSerializer(read_only=True)
    asignatura = AsignaturaSerializer(read_only=True)
    periodo = PeriodoSerializer(read_only=True)

    class Meta:
        model = Calificacion
        fields = '__all__'
