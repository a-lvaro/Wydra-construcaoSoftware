from sqlalchemy.exc import DBAPIError

from core.exceptions import BadRequestException, NotFoundException
from core.security import JWTHandler, PasswordHandler

from app.schemas.usuario import Usuario, UsuarioCreate, UsuarioUpdate
from app.models import Usuario as ormUsuario
from app.controllers.usuario import ControladorUsuario


class ControladorAuth(ControladorUsuario):
    def register(self, new_user: UsuarioUpdate) -> ormUsuario:
        if new_user.senha != new_user.senha_confirma:
            raise BadRequestException(detail="As senhas não batem.")
        
        new_user.senha = PasswordHandler.hash(new_user.senha)

        try:
            db_user = self.create(new_user)
        except DBAPIError:
            raise BadRequestException(detail="Já existe um usuário com esse nick ou email.")

        return db_user

    def login(self, nick: str, senha: str) -> str:
        user = self.get_by_nick(nick)

        if not PasswordHandler.verify(user.senha, senha):
            raise BadRequestException("Senha incorreta.")

        access_token = JWTHandler.encode(payload={"usuario_id": user.id})
        return access_token

    def get_by_token(self, token: str) -> ormUsuario:
        payload = JWTHandler.decode(token)
        id = payload['usuario_id']

        user = self.get(id)
        return user

    def get_user(self, token: str) -> ormUsuario:
        payload = JWTHandler.decode(token)
        id = payload['usuario_id']

        user = self.get(id)
        return user

    def edit(self, token: str, perfil: UsuarioCreate) -> ormUsuario:
        user = self.get_by_token(token)

        if perfil.senha != perfil.senha_confirma:
            raise BadRequestException(detail="As senhas não batem.")
        
        super().edit(user, perfil)

        return user
        