from datetime import datetime
from pydantic import EmailStr

from app.schemas.usuario import Usuario, UsuarioCreate, Perfil
from app.models.usuario import Usuario as ormUsuario


class ControladorUsuario:
    def __init__(self, session):
        self.session = session

    async def get(self, id: int) -> Usuario:
        user = self.session.query(ormUsuario).filter(
            ormUsuario.id == id).first()
        print(user)

        return user

    async def get_by_nick(self, nick: str):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nick == nick).first()
        return user

    async def search_by_nick(self, nick: str, skip: int = 0, limit: int = 100):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nick.contains(nick)).offset(skip).limit(limit).all()
        return user

    async def get_by_email(self, email: EmailStr):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.email == email).first()
        return user

    async def search_by_nome(self, nome: str, skip: int = 0, limit: int = 100):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nome.contains(nome)).offset(skip).limit(limit).all()
        return user

    async def create(self, user: UsuarioCreate) -> Usuario:
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

        return db_user

    async def editar_perfil(self, id: int,  perfil: Perfil) -> Perfil:
        usuario = self.session.query(ormUsuario).filter(
            ormUsuario.id == id).first()

        usuario.nome = perfil.nome
        usuario.sobrenome = perfil.sobrenome
        usuario.nick = perfil.nick
        usuario.email = perfil.email
        usuario.senha = perfil.senha

        self.session.commit()
        self.session.refresh(usuario)

        return Perfil.from_orm(usuario)
