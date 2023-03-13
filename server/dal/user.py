from typing import List
import hashlib

from domain import schemas
from . import orm 

# Implementa o padrão repositório
# para a classe Usuario
class Repository:
    def __init__(self, session):
        self.session = session

    def get(self, id : int) -> schemas.Usuario:
        return self.session.query(orm.Usuario).filter(orm.Usuario.id == id).first()

    def get_by_email(self, email : str) -> schemas.Usuario:
        return self.session.query(orm.Usuario).filter(orm.Usuario.email == email).first()

    def get_by_nome(self, nome : str, skip : int = 0, limit : int = 100) -> List[schemas.Usuario]:
        return self.session.query(orm.Usuario).filter(nome in orm.Usuario.nome).offset(skip).limit(limit).all()

    def create(self, user : schemas.UsuarioCreate) -> schemas.Usuario:
        self.session.add(user)
        
        self.session.commit()
        self.session.refresh(db_user)

        return self.get(db_user.id)

    def delete(self, id : int):
        user = self.session.query(orm.Usuario).filter(orm.Usuario.id == id).first()
        
        self.session.delete(user)
        self.session.commit()

