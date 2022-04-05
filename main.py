"""
Além das duas bibliotecas abaixo instalar também o
uvicorn: pip  install uvicorn
e para rodar no navegador: uvicorn main:app --reload (assim ele da reload automatico)

está funcionando porém preciso descobrir como persistir os dados

pip install httpie -> serve para testar requisições via terminal

tinyDB para persistir os dados (implementar)
https://tinydb.readthedocs.io/en/latest/getting-started.html
"""
from fastapi import FastAPI  # parece ser o mais moderno tem que ver o flask
from fastapi.middleware.cors import CORSMiddleware  # serve para permitir o acesso do front
from pydantic import BaseModel  # para instanciar objetos
from tiny import db, User, where

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


# Rota raiz
@app.get("/")
def root():
    return {"API": "Magano"}


# Criar Model
class Usuario(BaseModel):
    id: int
    email: str
    senha: str


# Criar Base de dados // usar tinyDB !!


# Rota gets ALL
@app.get("/usuarios")
def get_todos_usuarios():
    """Retorna todos os usuários"""
    return db.all()


# Rota get Id
@app.get("/usuarios/{id_usuario}")
def get_usuario_id(id_usuario: int):
    for usuario in db:
        if usuario['id'] == id_usuario:
            return usuario
    return {"Status": 400, "Mensagem": "Usuário não localizado!"}


# Rota POST usuário
@app.post("/usuarios")
def insere_usuario(usuario: Usuario):
    """  # Fazer uma tratativa caso exista um id igual """
    if usuario in db:
        print(dict(usuario))
        return {"Status": 400, "Mensagem": "Usuário ja existe!"}
    print(f'{usuario} adicionado com sucesso!')
    db.insert(dict(usuario))
    return {"Status": 200, "Mensagem": "Usuário adicionado"}


@app.delete("/usuarios/{id_usuario}")
def deleta_usuario(id_usuario: int):
    for usuario in db:
        if usuario['id'] == id_usuario:
            db.remove(User.id == usuario['id'])
            print(usuario)
            return {"Status": 200, "Mensagem": "Usuário removido"}
    return {"Status": 400, "Mensagem": "Usuário não localizado!"}


@app.patch("/usuarios/{id_usuario}")
def altera_dados(id_usuario: int, email: str, senha: str):
    for user in db:
        if user['id'] == id_usuario:
            db.update({"email": email}, User.id == user['id'])  # User.id == Query().id == novo_id
            db.update({"senha": senha}, User.id == user['id'])  # primeiro dado é o que vai ser alterado o segundo onde
            return {"Status": 200, "Mensagem": "Dados atualizados"}
    return {"Status": 400, "Mensagem": "Usuário não localizado!"}


@app.get("/usuarios/{email}")
def pesquisa_por_email(email: str):
    res = db.search(User['email'] == email)
    print(res)
    return {"Status": 200, "Mensagem": "Dados atualizados"}
