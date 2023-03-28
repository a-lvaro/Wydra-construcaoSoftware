from core.exceptions import BadRequestException
from core.security import JWTHandler, PasswordHandler

from app.schemas.usuario import Usuario, UsuarioCreate

from app.controllers.usuario import UserController


class AuthController(UserController):
    async def register(self, new_user: UsuarioCreate) -> Usuario:
        # Check if Usuario exists with nick
        user = await self.get_by_nick(new_user.nick)

        if user:
            raise BadRequestException("Já existe um usuário com esse nick.")

        # Check if Usuario exists with nick
        user = await self.get_by_nick(new_user.nick)

        if user:
            raise BadRequestException("Já existe um usuário com esse nick.")

        new_user.senha = PasswordHandler.hash(new_user.senha)

        return await self.create(new_user)

    async def login(self, nick: str, senha: str) -> str:
        user = await self.get_by_nick(nick)

        if not user:
            raise BadRequestException("Usuário não existe.")

        if not PasswordHandler.verify(user.senha, senha):
            raise BadRequestException("Senha incorreta.")

        access_token = JWTHandler.encode(payload={"usuario_id": user.id})
        return access_token

    async def get_user(self, token: str) -> Usuario:
        payload = JWTHandler.decode(token)
        id = payload['usuario_id']

        user = await self.get(id)
        return user
