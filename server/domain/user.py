from fastapi import HTTPException

from domain import schemas
from dal import UserRepository
from dal.orm import Session

# Classe generica para o controlador de usuário
# recebe um repositório genérico e pode ser usada para testes
class GenericController:
    def __init__(self, repository):
        self.repository = repository 

    def get(self, id : int):
        user = self.repository.get(id)
         
        if not user:
            raise HTTPException(status_code=404, detail="Usuário não existe.")

        return user

    def create(self, user : schemas.UserCreate):
        if not (user.name and user.email and user.password):
            raise HTTPException(status_code=400, detail="Informações inválidas.")
        elif self.repository.get_by_email(user.email):
            raise HTTPException(status_code=400, detail="Email já cadastrado.")

        user = self.repository.create(user)
        return user

# Classe para o controlador do usuário
# Acessa diretamente o banco de dados através
# de um repositório
class Controller(GenericController):
    def __init__(self):
        db = Session()
        self.repository = UserRepository(db)

