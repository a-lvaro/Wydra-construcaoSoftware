from pydantic import EmailStr

from core.exceptions import NotFoundException
from app.schemas import Usuario, UsuarioCreate
from app.models import Usuario as ormUsuario


class ControladorUsuario:
    def __init__(self, session):
        self.session = session

    def get(self, id: int) -> ormUsuario:
        user = self.session.query(ormUsuario).filter(
            ormUsuario.id == id).first()

        if not user:
            raise NotFoundException(detail="Usuário não existe.")

        return user

    def get_by_nick(self, nick: str):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nick == nick).first()

        if not user:
            raise NotFoundException(detail="Usuário não existe.")

        return user

    def search_by_nick(self, nick: str, skip: int = 0, limit: int = 100):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nick.contains(nick)).offset(skip).limit(limit).all()

        return user

    def get_by_email(self, email: EmailStr):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.email == email).first()

        if not user:
            raise NotFoundException(detail="Usuário não existe.")

        return user

    def search_by_nome(self, nome: str, skip: int = 0, limit: int = 100):
        user = self.session.query(ormUsuario).filter(
            ormUsuario.nome.contains(nome)).offset(skip).limit(limit).all()
        return user

    def create(self, user: UsuarioCreate):
        db_user = ormUsuario(user.nick, user.nome, user.sobrenome,
                             user.email, user.senha, user.caminho_foto)

        self.session.add(db_user)
        self.session.commit()

        return db_user

    def edit(self, db_usuario: ormUsuario,  perfil: UsuarioCreate):
        db_usuario = self.get(id)

        db_usuario.nome = perfil.nome
        db_usuario.sobrenome = perfil.sobrenome
        db_usuario.nick = perfil.nick
        db_usuario.email = perfil.email
        db_usuario.senha = perfil.senha
        db_usuario.caminho_foto = perfil.caminho_foto

        self.session.commit()

        return db_usuario



