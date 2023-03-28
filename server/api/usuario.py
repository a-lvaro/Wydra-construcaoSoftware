from typing import List
from fastapi import APIRouter

from app.controllers.usuario import UserController
from app.controllers.auth import AuthController

from app.schemas.usuario import UsuarioCreate, Usuario, UsuarioAuth

from core.security import JWTHandler
from core.database import get_session

userRouter = APIRouter(
    prefix="/user"
)

@userRouter.post("/signup", status_code=201, response_model=Usuario)
async def register_user(user: UsuarioCreate):
    db = get_session()
    auth_controller = AuthController(db)

    return await auth_controller.register(user)

@userRouter.post("/login")
async def login_user(login_user_request: UsuarioAuth) -> str:
    db = get_session()
    auth_controller = AuthController(db)

    return await auth_controller.login(
        email=login_user_request.email, password=login_user_request.senha
    )

@userRouter.get("/me")
async def get_current_user(access_token: str) -> Usuario:
    db = get_session()
    auth_controller = AuthController(db)

    user = await auth_controller.get_user(access_token)
    return user


@userRouter.get("/search")
async def search_user(nick: str) -> List[Usuario]:
    db = get_session()
    user_controller = UserController(db)
    results = await user_controller.search_by_nick(nick)
    return results


@userRouter.get("/")
async def get_user(nick: str) -> Usuario:
    db = get_session()
    user_controller = UserController(db)

    users = await user_controller.get_by_nick(nick)

    return users