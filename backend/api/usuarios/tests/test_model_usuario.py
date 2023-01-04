from django.forms import ValidationError
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

    def test_criado_em(self):
        """O usuário precisa ter um atributo auto-criado referente à data de criação do registro"""
        self.assertIsInstance(self.obj.criado_em, datetime)

    def test_ativo(self):
        """O usuário precisa ter um atributo (boolean) auto-criado informando se o usuário está ativo ou não"""
        self.assertIsInstance(self.obj.ativo, bool)

    def test_usuario_ativo_por_padrao(self):
        """Testa se o usuário por padrão está ativo"""
        self.assertEqual(True, self.obj.ativo)

    def test_representacao_string_do_modelo(self):
        """Testa se a representação em string do modelo é igual ao nome do usuário"""
        self.assertEqual("Usuário Teste", str(self.obj))

    def test_tamanho_maximo_nome_do_usuario(self):
        """Testa se o tamanho máximo de 100 caracteres do nome do usuário está sendo respeitado"""
        with self.assertRaises(ValidationError):
            Usuario(
                nome="A" * 101, email="email@email.com", senha="senha123"
            ).full_clean()
        Usuario(nome="A" * 100, email="email@email.com", senha="senha123").full_clean()

    def test_nome_do_usuario_vazio(self):
        """Não deve ser possível registrar um usuário com nome vazio"""
        for content in ["", None]:
            with self.subTest():
                with self.assertRaises(ValidationError):
                    Usuario(
                        nome=content,
                        email="email@email.com",
                        senha="senha123",
                    ).full_clean()
