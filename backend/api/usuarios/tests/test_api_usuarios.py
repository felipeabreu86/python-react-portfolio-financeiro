from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


class UsuariosTestCase(APITestCase):
    def setUp(self):
        """Configura os detalhes iniciais para os testes serem executados"""
        self.user_model = get_user_model()
        self.csrf_token = ""

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
        self.csrf_token = self.client.cookies["csrftoken"].value
        self.assertEquals(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEquals(True, len(self.csrf_token) > 0)

    def test_requisicao_post_para_autenticar_um_usuario_inexistente(self):
        """Não deve ser permitida a autenticação de um usuário inexistente via método POST /usuarios/login"""
        data = {
            "username": "usuarioteste2",
            "password": "senha123",
        }
        response = self.client.post("/usuarios/auth/", data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)

    ### Testes de Criação de Usuário - /usuarios/create

    def test_requisicao_post_para_criar_um_usuario(self):
        """Deve-se criar um novo usuário via POST /usuarios/create"""
        data = {
            "username": "usuarioteste2",
            "password": "senha1234",
            "email": "usuarioteste2@email.com",
            "first_name": "Usuario",
            "last_name": "Teste",
        }
        response = self.client.post("/usuarios/create/", data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_requisicao_post_nao_permite_criar_usuario_com_username_vazio(self):
        """Não deve ser permitida a criação de um novo usuário com username vazio via POST /usuarios/create"""
        for content in ["", " "]:
            with self.subTest():
                data = {
                    "username": content,
                    "password": "senha1234",
                    "email": "usuarioteste2@email.com",
                    "first_name": "Usuario",
                    "last_name": "Teste",
                }
                response = self.client.post("/usuarios/create/", data=data)
                self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEquals(
                    "Este campo não pode ser em branco.", response.data["username"][0]
                )

    def test_requisicao_post_nao_permite_criar_usuario_sem_username(self):
        """Não deve ser permitida a criação de um novo usuário sem username via POST /usuarios/create"""
        data = {
            "password": "senha123",
            "email": "usuarioteste2@email.com",
            "first_name": "Usuario",
            "last_name": "Teste",
        }
        response = self.client.post("/usuarios/create/", data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals("Este campo é obrigatório.", response.data["username"][0])

    def test_requisicao_post_nao_permite_criar_usuario_com_senha_vazia(self):
        """Não deve ser permitida a criação de um novo usuário com senha vazia via POST /usuarios/create"""
        data = {
            "username": "usuarioteste3",
            "password": "",
            "email": "usuarioteste2@email.com",
            "first_name": "Usuario",
            "last_name": "Teste",
        }
        response = self.client.post("/usuarios/create/", data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals(
            "Este campo não pode ser em branco.", response.data["password"][0]
        )

    def test_requisicao_post_nao_permite_criar_usuario_sem_senha(self):
        """Não deve ser permitida a criação de um novo usuário sem senha via POST /usuarios/create"""
        data = {
            "username": "usuarioteste3",
            "email": "usuarioteste2@email.com",
            "first_name": "Usuario",
            "last_name": "Teste",
        }
        response = self.client.post("/usuarios/create/", data=data)
        self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEquals("Este campo é obrigatório.", response.data["password"][0])

    def test_requisicao_post_nao_permite_criar_usuario_com_senha_invalida(self):
        """
        Não deve ser permitida a criação de um novo usuário com senha inválida via POST /usuarios/create.
        A senha deve conter pelo menos 8 dígitos possuindo ao menos uma letra e um número.
        """
        for content in [
            "aaaaaa1",
            "123456a",
            "aaaaaaaa",
            "12345678",
            "!@*!@*!@",
            "!@*!@*!1",
            "!@*!@*!a",
            " ",
        ]:
            with self.subTest():
                data = {
                    "username": "usuarioteste3",
                    "password": content,
                    "email": "usuarioteste2@email.com",
                    "first_name": "Usuario",
                    "last_name": "Teste",
                }
                response = self.client.post("/usuarios/create/", data=data)
                self.assertEquals(response.status_code, status.HTTP_400_BAD_REQUEST)
                self.assertEquals(
                    "Este valor não corresponde ao padrão exigido.",
                    response.data["password"][0],
                )
