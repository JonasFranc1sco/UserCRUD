# UserCRUD

Sistema de cadastro de usuários com funcionalidades completas de CRUD, desenvolvido com Django, utilizando PostgreSQL como banco de dados, e rodando via Docker.

---

## Tecnologias

- Python 3
- Django
- PostgreSQL
- Docker e Docker Compose

---

## Pré-requisitos

- Docker instalado: https://docs.docker.com/get-docker/

---

## Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/UserCRUD.git
cd userCrud
```
### 2. Crie o arquivo .env
Use o arquivo .env.example como base:
```bash
cp .env.example .env
```
Edite o .env com suas configurações:
Dica: gere uma secret key segura em https://djecrety.ir/
```bash
DJANGO_SECRET_KEY=sua_chave_secreta
DEBUG=True
DJANGO_LOGLEVEL=info
DJANGO_ALLOWED_HOSTS=localhost

DATABASE_ENGINE=postgresql_psycopg2
DATABASE_NAME=usercrud_db
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=senha_segura
DATABASE_HOST=db
DATABASE_PORT=5432
```
## Como rodar o projeto
Suba os containers com Docker Compose:
```bash
docker compose up --build
```
A aplicação estará disponível em:
```bash
http://localhost:8000/
```
## Rotas da aplicação
Registro de novo usuário: http://localhost:8000/

Login de usuário: http://localhost:8000/login

Leitura de usuários cadastrados: http://localhost:8000/read/

Atualizar usuário: http://localhost:8000/user/update/<user_id>

Deletar usuário: http://localhost:8000/user/delete/<user_id>

(Substitua <user_id> pelo ID do usuário no banco)

## Comandos úteis
### Aplicar as migrations
```bash
docker compose exec django-web python manage.py migrate
```

### Criar um superusuário
```bash
docker compose exec django-web python manage.py createsuperuser
```
