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
    with get_session() as db:
        auth_controller = ControladorAuth(db)
        user = auth_controller.register(user)

        return Usuario.from_orm(user)


@userRouter.post("/login")
def login(login_user_request: UsuarioAuth) -> str:
    with get_session() as db:
        auth_controller = ControladorAuth(db)

        token = auth_controller.login(
            nick=login_user_request.nick, senha=login_user_request.senha
        )

        return token


@userRouter.get("/me")
def get_current_user(access_token: str) -> Usuario:
    with get_session() as db:
        auth_controller = ControladorAuth(db)
        user = auth_controller.get_by_token(access_token)

        return Usuario.from_orm(user)


@userRouter.get("/search")
def search_user(nick: str) -> List[Usuario]:
    with get_session() as db:
        user_controller = ControladorUsuario(db)
        results = user_controller.search_by_nick(nick)

        return [Usuario.from_orm(user) for user in results]


@userRouter.get("/{nick}")
def get_user(nick: str) -> Usuario:
    with get_session() as db:
        user_controller = ControladorUsuario(db)
        user = user_controller.get_by_nick(nick)

        return Usuario.from_orm(user)


@userRouter.put("/editar")
def edit_user(perfil: Perfil, access_token: str) -> Perfil:
    with get_session() as db:
        auth_controller = ControladorAuth(db)
        user = auth_controller.get_user(access_token)
        user = auth_controller.edit(user.id, perfil)

        return Perfil.from_orm(user)
