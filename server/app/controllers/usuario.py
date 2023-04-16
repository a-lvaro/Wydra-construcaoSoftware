from pydantic import EmailStr
from pathlib import Path
import binascii
import codecs

from core.exceptions import NotFoundException, BadRequestException
from app.schemas import Usuario, UsuarioCreate, UsuarioUpdate
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

    def update_photo(self, user: ormUsuario, foto, ext):
        try:
            user.caminho_foto = f"static/profile/{user.nick}.{ext}"
            Path(user.caminho_foto).write_bytes(codecs.decode(foto, "base64"))
        except binascii.Error:
            raise BadRequestException(detail="Imagem inválida. O arquivo precisa ser criptogafado em Base64.")

    def create(self, user: UsuarioCreate):

        db_user = ormUsuario(user.nick, user.nome, user.sobrenome,
                             user.email, user.senha)

        if not user.foto:
            user.caminho_foto = "static/default.jpg"
        else:
            self.update_photo(db_user, user.foto, user.foto_ext)

        self.session.add(db_user)
        self.session.commit()

        return db_user

    def edit(self, db_usuario: ormUsuario,  perfil:  UsuarioUpdate):
        if perfil.nome:
            db_usuario.nome = perfil.nome

        if perfil.sobrenome:
            db_usuario.sobrenome = perfil.sobrenome

        if perfil.email:
            db_usuario.email = perfil.email

        if perfil.senha:
            if perfil.senha != perfil.senha_confirma:
                raise BadRequestException(detail="As senhas não batem.")
                
            db_usuario.senha = perfil.senha

        if perfil.foto:
            self.update_photo(db_usuario, perfil.foto, perfil.foto_ext)

        self.session.commit()

        return db_usuario



