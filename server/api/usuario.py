from typing import List
from fastapi import APIRouter

from app.controllers import ControladorUsuario
from app.controllers import ControladorAuth

from app.schemas import UsuarioCreate, Usuario, UsuarioAuth, Perfil

from core.database import get_session

userRouter = APIRouter(
    prefix="/user"
)


@userRouter.post("/signup", status_code=201, response_model=Usuario)
def register(user: UsuarioCreate):
    db = get_session()
    auth_controller = ControladorAuth(db)

    return auth_controller.register(user)


@userRouter.post("/login")
def login(login_user_request: UsuarioAuth) -> str:
    db = get_session()
    auth_controller = ControladorAuth(db)

    return auth_controller.login(
        nick=login_user_request.nick, senha=login_user_request.senha
    )


@userRouter.get("/me")
def get_current_user(access_token: str) -> Usuario:
    db = get_session()
    auth_controller = ControladorAuth(db)

    user = auth_controller.get_by_token(access_token)
    return user


@userRouter.get("/search")
def search_user(nick: str) -> List[Usuario]:
    db = get_session()
    user_controller = ControladorUsuario(db)
    results = user_controller.search_by_nick(nick)
    return results


@userRouter.get("/{nick}")
def get_user(nick: str) -> Usuario:
    db = get_session()
    user_controller = ControladorUsuario(db)

    users = user_controller.get_by_nick(nick)

    return users


@userRouter.put("/editar")
def edit_user(perfil: Perfil, access_token: str) -> Perfil:
    db = get_session()
    auth_controller = ControladorAuth(db)

    user = auth_controller.get_user(access_token)

    return auth_controller.edit(user.id, perfil)
