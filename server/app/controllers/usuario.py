from datetime import datetime

from app.schemas.usuario import Usuario, UsuarioCreate
from app.models.usuario import Usuario as ormUsuario

class Controlador:
    def __init__(self, session):
        self.session = session

    def get(self, id: int) -> Usuario:
        user = self.session.query(ormUsuario).filter(
            ormUsuario.id == id).first()
        return user

    def get_by_nick(self, nick: str):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nick == nick).first()
        return user

    def search_by_nick(self, nick: str, skip: int = 0, limit: int = 100):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nick.contains(nick)).offset(skip).limit(limit).all()
        return user

    def get_by_email(self, email: str):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.email == email).first()
        return user

    def search_by_nome(self, nome: str, skip: int = 0, limit: int = 100):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nome.contains(nome)).offset(skip).limit(limit).all()
        return user

    def create(self, user: UsuarioCreate) -> Usuario:
        db_user = ormUsuario()

        db_user.nome = user.nome
        db_user.sobrenome = user.sobrenome
        db_user.nick = user.nick

        db_user.email = user.email
        db_user.senha = user.senha
        db_user.data_cadastro = datetime.utcnow()

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        user = self.get(db_user.id)

        return Usuario.from_orm(user)

    def delete(self, id: int):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.id == id).first()

        self.session.delete(user)
        self.session.commit()
