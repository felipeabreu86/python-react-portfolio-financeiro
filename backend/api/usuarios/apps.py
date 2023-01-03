from django.apps import AppConfig


class UsuariosConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "api.usuarios"
    verbose_name: str = "Controle de Usuários"
