from django.contrib import admin
from api.usuarios.models import Usuario


class UsuarioModelAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "senha", "criado_em", "ativo")
    date_hierarchy = "criado_em"
    search_fields = ("nome", "email", "criado_em", "ativo")


admin.site.register(Usuario, UsuarioModelAdmin)
