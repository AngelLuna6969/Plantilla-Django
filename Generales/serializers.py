from rest_framework import serializers
from .models import Modelo

class ModeloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modelo
        exclude = ('archivo', 'foto')  # Excluye 'archivo' y 'foto'
