from rest_framework.test import APITestCase
from rest_framework import status


class UsuariosTestCase(APITestCase):
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
