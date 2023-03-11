from fastapi import HTTPException

from domain import schemas
from dal import userRepository
from dal.orm import Session

class Controller:
    def __init__(self):
        db = Session()
        self.repository = userRepository(db)

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
