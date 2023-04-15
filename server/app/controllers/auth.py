from core.exceptions import BadRequestException, NotFoundException
from core.security import JWTHandler, PasswordHandler

from app.schemas.usuario import Usuario, UsuarioCreate
from app.controllers.usuario import ControladorUsuario


class ControladorAuth(ControladorUsuario):
    def register(self, new_user: UsuarioCreate) -> Usuario:
        # Check if Usuario exists with nick

        try:
            user = self.get_by_nick(new_user.nick)

            if user:
                raise BadRequestException(
                    "Já existe um usuário com esse nick.")
        except NotFoundException:
            pass

        new_user.senha = PasswordHandler.hash(new_user.senha)

        return self.create(new_user)

    def login(self, nick: str, senha: str) -> str:
        user = self.get_by_nick(nick)

        if not PasswordHandler.verify(user.senha, senha):
            raise BadRequestException("Senha incorreta.")

        access_token = JWTHandler.encode(payload={"usuario_id": user.id})
        return access_token

    def get_by_token(self, token: str) -> Usuario:
        payload = JWTHandler.decode(token)
        id = payload['usuario_id']

        user = self.get(id)
        return user

    def get_user(self, token: str) -> Usuario:
        payload = JWTHandler.decode(token)
        id = payload['usuario_id']

        user = self.get(id)
        return user
