from pydantic import EmailStr

from core.exceptions import NotFoundException
from app.schemas import Usuario, UsuarioCreate, Perfil
from app.models import Usuario as ormUsuario


class ControladorUsuario:
    def __init__(self, session):
        self.session = session

    def get(self, id: int) -> Usuario:
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

    def create(self, user: UsuarioCreate) -> Usuario:
        db_user = ormUsuario(user.nick, user.nome, user.sobrenome,
                             user.email, user.senha, user.caminho_foto)

        self.session.add(db_user)
        self.session.commit()
        self.session.refresh(db_user)

        return db_user

    def edit(self, id: int,  perfil: Perfil) -> Perfil:
        usuario = self.get(id)

        usuario.nome = perfil.nome
        usuario.sobrenome = perfil.sobrenome
        usuario.nick = perfil.nick
        usuario.email = perfil.email

        self.session.commit()
        self.session.refresh(usuario)

        return Perfil.from_orm(usuario)
