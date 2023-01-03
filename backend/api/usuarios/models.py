from django.db import models


class Usuario(models.Model):
    nome = models.CharField("nome", max_length=100)
    email = models.EmailField("e-mail")
    senha = models.CharField("senha", max_length=10)
    ativo = models.BooleanField("ativo", default=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome
