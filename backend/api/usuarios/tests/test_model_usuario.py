from django.test import TestCase
from api.usuarios.models import Usuario
from datetime import datetime


class UsuarioModelTest(TestCase):
    def setUp(self):
        self.obj = Usuario(
            nome="Usuário Teste",
            email="email@email.com",
            senha="senha123",
        )
        self.obj.save()

    def test_usuario_criado(self):
        """Testa a criação de um usuário"""
        self.assertTrue(Usuario.objects.exists())

    def test_created_at(self):
        """O usuário precisa ter um atributo auto-criado referente à data de criação do registro"""
        self.assertIsInstance(self.obj.criado_em, datetime)

    def test_representacao_string_do_modelo(self):
        """Testa se a representação em string do modelo é igual ao nome do usuário"""
        self.assertEqual("Usuário Teste", str(self.obj))

    def test_usuario_ativo_por_padrao(self):
        """Testa se o usuário por padrão está ativo"""
        self.assertEqual(True, self.obj.ativo)
