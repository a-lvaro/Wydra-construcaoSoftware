from datetime import datetime

from model import schema
from model import orm


class ControladorUsuario:
    def __init__(self, session):
        self.session = session

    def get(self, id: int) -> schema.Usuario:
        user = self.session.query(orm.Usuario).filter(
            orm.Usuario.id == id).first()
        return user

    def get_by_nick(self, nick: str):
        user = self.session.query(orm.Usuario).filter(
            orm.Usuario.nick == nick).first()
        return user

    def search_by_nick(self, nick: str, skip: int = 0, limit: int = 100):
        user = self.session.query(orm.Usuario).filter(
            orm.Usuario.nick.contains(nick)).offset(skip).limit(limit).all()
        return user

    def get_by_email(self, email: str):
        user = self.session.query(orm.Usuario).filter(
            orm.Usuario.email == email).first()
        return user

    def search_by_nome(self, nome: str, skip: int = 0, limit: int = 100):
        user = self.session.query(orm.Usuario).filter(
            orm.Usuario.nome.contains(nome)).offset(skip).limit(limit).all()
        return user

    def create(self, user: schema.UsuarioCreate) -> schema.Usuario:
        db_user = orm.Usuario()

        db_user.nome = user.nome
        db_user.sobrenome = user.sobrenome
        db_user.nick = user.nick

        db_user.email = user.email
        db_user.senha = user.senha
        db_user.data_cadastro = datetime.now()

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        user = self.get(db_user.id)

        return schema.Usuario.from_orm(user)

    def delete(self, id: int):
        user = self.session.query(orm.Usuario).filter(
            orm.Usuario.id == id).first()

        self.session.delete(user)
        self.session.commit()
