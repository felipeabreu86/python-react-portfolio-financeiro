# Portfólio Financeiro Web

Sistema Web desenvolvido com Django (Backend) e React (Frontend) visando manter um portfólio financeiro pessoal.

## Backend
### Como Desenvolver (Windows):

1. Clone o repositório
2. Acesse via terminal o diretório 'backend'
3. Crie um virtualenv utilizando **Python 3.11.1**
4. Ative o virtualenv
5. Instale as dependências
6. Configure a instância com o **.env**
7. Execute os testes

```console
1. git clone git@github.com:felipeabreu86/python-django-rest-api-clientes.git
2. cd python-django-rest-api-clientes\backend
3. python -m venv .venv
4. ./.venv/scripts/activate
5. pip install -r requirements.txt
6. cp .dev-contrib/env-sample .env
7. python manage.py test
```

### Como Realizar o Deploy (Windows):

1. Tenha/Crie uma conta no **Fly.io**
2. Configure as variáveis de ambiente não-sensíveis em **fly.toml** dentro de **[env]**
3. Instale o Fly CLI (flyctl)
4. Autentique-se via flyctl
5. Realize o Deploy
6. Configure uma variável de ambiente sensível chamada **SECRET_KEY**
7. Configure um super usuário para a aplicação
8. Consulte todas as variáveis de ambiente configuradas

```console
3. iwr https://fly.io/install.ps1 -useb | iex
4. flyctl auth login
5. flyctl deploy
6. flyctl secrets set SECRET_KEY=<chave-secreta-aqui>
7. flyctl ssh console -C 'python /code/manage.py createsuperuser'
8. flyctl ssh console -C "printenv"
```

## Frontend

### Como Desenvolver (Windows):

### Como Realizar o Deploy (Windows):