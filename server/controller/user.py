from fastapi import HTTPException
from typing import List
from bcrypt import checkpw

from model.orm import Session
from model import schema
from model import orm 


class Controlador:
    def __init__(self, session):
        self.session = session

    def get(self, id : int) -> schema.Usuario:
        user = self.session.query(orm.Usuario).filter(orm.Usuario.id == id).first()

        if not user:
            raise HTTPException(status_code=404, detail="Usuário não existe.") 

        return user

    def get_by_email(self, email : str) -> schema.Usuario:
        return self.session.query(orm.Usuario).filter(orm.Usuario.email == email).first()

    def get_by_nome(self, nome : str, skip : int = 0, limit : int = 100) -> List[schema.Usuario]:
        return self.session.query(orm.Usuario).filter(nome in orm.Usuario.nome).offset(skip).limit(limit).all()

    def create(self, user : schema.UsuarioCreate) -> schema.Usuario:
        if not (user.nome and user.email and user.senha):
            raise HTTPException(status_code=400, detail="Informações inválidas.")
        elif self.get_by_email(user.email):
            raise HTTPException(status_code=400, detail="Email já cadastrado.")

        db_user = orm.Usuario(user.nome, user.email, user.senha)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return self.get(db_user.id)

    def delete(self, id : int):
        user = self.session.query(orm.Usuario).filter(orm.Usuario.id == id).first()
        
        self.session.delete(user)
        self.session.commit()
    
def getControlador():
    db = Session()
    return Controlador(db)
