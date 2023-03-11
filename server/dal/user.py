from typing import List
import hashlib

from domain import schemas
from . import orm 

# Implementa o padrão repositório
# para a classe User
class Repository:
    def __init__(self, session):
        self.session = session

    def get(self, id : int) -> schemas.User:
        return self.session.query(orm.User).filter(orm.User.id == id).first()

    def get_by_email(self, email : str) -> schemas.User:
        return self.session.query(orm.User).filter(orm.User.email == email).first()

    def get_by_name(self, name : str, skip : int = 0, limit : int = 100) -> List[schemas.User]:
        return self.session.query(orm.User).filter(name in orm.User.name).offset(skip).limit(limit).all()

    def create(self, user : schemas.UserCreate) -> schemas.User:
        hashed = hashlib.sha256(user.password.encode()).hexdigest()

        db_user = orm.User(name=user.name, email=user.email, password=hashed)
        self.session.add(db_user)
        
        self.session.commit()
        self.session.refresh(db_user)

        return self.get(db_user.id)

    def delete(self, id : int):
        user = self.session.query(orm.User).filter(orm.User.id == id).first()
        
        if user:
            self.session.delete(user)
            self.session.commit()

