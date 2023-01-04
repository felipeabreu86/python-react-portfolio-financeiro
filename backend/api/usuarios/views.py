from rest_framework import viewsets
from .serializers import UsuariosSerializer

from .models import Usuario


class UsuariosViewSet(viewsets.ModelViewSet):
    serializer_class = UsuariosSerializer
    queryset = Usuario.objects.all()
    http_method_names = ["post", "put", "path", "delete"]
