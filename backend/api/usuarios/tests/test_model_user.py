from django.forms import ValidationError
from django.test import TestCase
from datetime import datetime
from django.contrib.auth import get_user_model

User = get_user_model()


class UserModelTest(TestCase):
    def setUp(self):
        self.obj = User(
            username="usuarioteste",
            email="email@email.com",
            password="senha123",
            first_name="Usuario",
            last_name="Teste",
        )
        self.obj.save()

    def test_usuario_criado(self):
        """Testa a criação de um usuário"""
        self.assertTrue(User.objects.exists())

    def test_criado_em(self):
        """O usuário precisa ter um atributo auto-criado referente à data de criação do registro"""
        self.assertIsInstance(self.obj.date_joined, datetime)

    def test_ativo(self):
        """O usuário precisa ter um atributo (boolean) auto-criado informando se o usuário está ativo ou não"""
        self.assertIsInstance(self.obj.is_active, bool)

    def test_usuario_ativo_por_padrao(self):
        """Testa se o usuário por padrão está ativo"""
        self.assertEqual(True, self.obj.is_active)

    def test_representacao_string_do_modelo(self):
        """Testa se a representação em string do modelo é igual ao nome do usuário"""
        self.assertEqual("usuarioteste", str(self.obj))

    def test_tamanho_maximo_nome_do_usuario(self):
        """Testa se o tamanho máximo de 150 caracteres do nome do usuário está sendo respeitado"""
        with self.assertRaises(ValidationError):
            User(
                username="A" * 151,
                email="email@email.com",
                password="senha123",
                first_name="Usuario",
                last_name="Teste",
            ).full_clean()
        User(
            username="A" * 150,
            email="email@email.com",
            password="senha123",
            first_name="Usuario",
            last_name="Teste",
        ).full_clean()

    def test_nome_do_usuario_vazio(self):
        """Não deve ser possível registrar um usuário com nome vazio"""
        for content in ["", None]:
            with self.subTest():
                with self.assertRaises(ValidationError):
                    User(
                        username=content,
                        email="email@email.com",
                        password="senha123",
                        first_name="Usuario",
                        last_name="Teste",
                    ).full_clean()

    def test_senha_do_usuario_vazia(self):
        """Não deve ser possível registrar um usuário com senha vazia"""
        for content in ["", None]:
            with self.subTest():
                with self.assertRaises(ValidationError):
                    User(
                        username="username",
                        email="email@email.com",
                        password=content,
                        first_name="Usuario",
                        last_name="Teste",
                    ).full_clean()
