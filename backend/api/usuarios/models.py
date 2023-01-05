from django.contrib.auth.models import AbstractUser


class UsuarioModel(AbstractUser):
    def __str__(self):
        return self.username
