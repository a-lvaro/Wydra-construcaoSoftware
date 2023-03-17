from fastapi import HTTPException
from typing import List
from bcrypt import checkpw

from model.orm import Session
from model import schemas
from model import orm 


class Controlador:
    def __init__(self, session):
        self.session = session

    def get(self, id : int) -> schemas.Usuario:
        user = self.session.query(orm.Usuario).filter(orm.Usuario.id == id).first()

        if not user:
            raise HTTPException(status_code=404, detail="Usuário não existe.") 

        return user

    def get_by_email(self, email : str) -> schemas.Usuario:
        return self.session.query(orm.Usuario).filter(orm.Usuario.email == email).first()

    def get_by_nome(self, nome : str, skip : int = 0, limit : int = 100) -> List[schemas.Usuario]:
        return self.session.query(orm.Usuario).filter(nome in orm.Usuario.nome).offset(skip).limit(limit).all()

    def create(self, user : schemas.UsuarioCreate):
        if not (user.nome and user.email and user.senha):
            raise HTTPException(status_code=400, detail="Informações inválidas.")
        elif self.get_by_email(user.email):
            raise HTTPException(status_code=400, detail="Email já cadastrado.")

        db_user = orm.Usuario(user.nome, user.email, user.senha)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

    def delete(self, id : int):
        user = self.session.query(orm.Usuario).filter(orm.Usuario.id == id).first()
        
        self.session.delete(user)
        self.session.commit()
    
    def authenticate(email, senha): 
        user = self.get_by_email(email)

        if user and checkpw(user.senha.encode('utf-8'), user.senha.encode('utf-8')):
            return user
        else:
            return None

def getControlador():
    db = Session()
    return Controlador(db)
