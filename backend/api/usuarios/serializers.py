from .models import Usuario
from rest_framework import serializers


class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        exclude = ["id", "senha"]
