from pydantic import EmailStr

from core.database import get_session

from core.exceptions import BadRequestException, UnauthorizedException
from core.security import JWTHandler, PasswordHandler

from app.schemas.usuario import Usuario, UsuarioCreate

from app.controllers.usuario import UserController


class AuthController(UserController):
    async def register(self, new_user : UsuarioCreate) -> Usuario:
        # Check if Usuario exists with email
        user = await self.get_by_email(new_user.email)

        if user:
            raise BadRequestException("Já existe um usuário com esse email.")

        # Check if Usuario exists with nick
        user = await self.get_by_nick(new_user.nick)

        if user:
            raise BadRequestException("Já existe um usuário com esse nick.")

        new_user.senha = PasswordHandler.hash(new_user.senha)

        return await self.create(new_user)

    async def login(self, email: EmailStr, password: str) -> str:
        user = await self.get_by_email(email)

        if not user:
            raise BadRequestException("Invalid credentials")

        if not PasswordHandler.verify(user.senha, password):
            raise BadRequestException("Invalid credentials")

        access_token = JWTHandler.encode(payload={"usuario_id": user.id})
        return access_token

    async def get_user(self, token: str) -> Usuario:
        payload = JWTHandler.decode(token)
        id = payload['usuario_id']
        
        user = await self.get(id)
        return user
         