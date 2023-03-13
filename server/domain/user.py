from fastapi import HTTPException
from bcrypt import checkpw, hashpw, gensalt
from datetime import datetime

from domain import schemas
from dal import RepositorioUsuario
from dal.orm import Session

# Classe para o controlador do usuário
# Acessa diretamente o banco de dados através
# de um repositório
class Controlador:
    def __init__(self, repository):
        self.repository = repository 

    def get(self, id : int) -> schemas.Usuario:
        user = self.repository.get(id)
         
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não existe.")

        return user

    def create(self, user : schemas.UsuarioCreate):
        if not (user.nome and user.email and user.senha):
            raise HTTPException(status_code=400, detail="Informações inválidas.")
        elif self.repository.get_by_email(user.email):
            raise HTTPException(status_code=400, detail="Email já cadastrado.")

        self.repository.create(user)

    def authenticate(email, senha): 
        user = self.repository.get_by_email(email)

        if user and checkpw(user.senha.encode('utf-8'), user.senha.encode('utf-8')):
            return user
        else:
            return None


def getControlador():
    db = Session()
    repo = RepositorioUsuario(db)

    return Controlador(repo)
