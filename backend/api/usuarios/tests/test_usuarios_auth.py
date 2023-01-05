from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class UsuariosTestCase(APITestCase):
    def setUp(self):
        """Configura os detalhes iniciais para os testes serem executados"""
        self.user_model = get_user_model()
        self.user_model.objects.create_user(
            username="usuarioteste1",
            email="email1@email.com",
            password="senha123",
            first_name="Usuario",
            last_name="Teste",
        ).save()

    ### Testes de Autenticação - /usuarios/auth

    def test_autenticacao_usuario(self):
        """Testa a autenticação de usuário criado para os testes"""
        assert self.client.login(username="usuarioteste1", password="senha123")

    def test_requisicao_post_para_autenticar_um_usuario(self):
        """Deve-se autenticar um usuário existente via método POST /usuarios/login"""
        data = {
            "username": "usuarioteste1",
            "password": "senha123",
        }
        response = self.client.post("/usuarios/auth/", data=data)
        csrf_token = self.client.cookies["csrftoken"].value
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEquals(True, len(csrf_token) > 0)

    def test_requisicao_post_para_autenticar_um_usuario_inexistente(self):
        """Não deve ser permitida a autenticação de um usuário inexistente via método POST /usuarios/login"""
        data = {
            "username": "usuarioteste2",
            "password": "senha123",
        }
        response = self.client.post("/usuarios/auth/", data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
