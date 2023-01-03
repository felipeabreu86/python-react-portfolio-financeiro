from django.db import models


class Usuario(models.Model):
    nome = models.CharField("nome", blank=False, max_length=100)
    email = models.EmailField("e-mail", blank=False)
    senha = models.CharField("senha", blank=False, max_length=10)
    ativo = models.BooleanField("ativo", default=True)
    criado_em = models.DateTimeField("criado em", auto_now_add=True)

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self):
        return self.nome
