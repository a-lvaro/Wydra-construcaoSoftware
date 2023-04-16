from typing import List
from fastapi import APIRouter

from core.config import Tags

from app.controllers import ControladorUsuario
from app.controllers import ControladorAuth

from app.schemas import UsuarioCreate, Usuario, UsuarioAuth, UsuarioUpdate

from core.database import get_session

userRouter = APIRouter(
    prefix="/user"
)

@userRouter.post(
    "/signup", 
    response_model=Usuario,
    summary="Cadastrar Usuário",
    description="Cadastra um novo usuário. O atributo `foto` deve ser a string resultante de um arquivo em bytes codificado em base64. Caso o usuário opte por não escolher uma foto, o atributo deve ser nulo.",
    tags=[Tags.user]
)
def register(user: UsuarioCreate):
    with get_session() as db:
        auth_controller = ControladorAuth(db)
        user = auth_controller.register(user)

        return Usuario.from_orm(user)


@userRouter.post(
    "/login",
    summary="Autenticar Usuário",
    description="Obtem um token de autenticação para o usuário.",
    tags=[Tags.user]
)
def login(login_user_request: UsuarioAuth) -> str:
    with get_session() as db:
        auth_controller = ControladorAuth(db)

        token = auth_controller.login(
            nick=login_user_request.nick, senha=login_user_request.senha
        )

        return token


@userRouter.get(
    "/me",
    summary="Usuário Atual",
    description="Retorna informações sobre o usuário portador do token.",
    tags=[Tags.user],
)
def get_current_user(access_token: str) -> Usuario:
    with get_session() as db:
        auth_controller = ControladorAuth(db)
        user = auth_controller.get_by_token(access_token)

        return Usuario.from_orm(user)


@userRouter.get(
    "/search",
    summary="Pesquisar Usuário",
    description="Pesquisa os usuários cujo nick contém a string `nick`",
    tags=[Tags.user]
)
def search_user(nick: str) -> List[Usuario]:
    with get_session() as db:
        user_controller = ControladorUsuario(db)
        results = user_controller.search_by_nick(nick)

        return [Usuario.from_orm(user) for user in results]


@userRouter.get(
    "/{nick}",
    summary="Perfil do Usuário",
    description="Obtem infromações sobre o usuário com o nick `nick`.",
    tags=[Tags.user]
)
def get_user(nick: str) -> Usuario:
    with get_session() as db:
        user_controller = ControladorUsuario(db)
        user = user_controller.get_by_nick(nick)

        return Usuario.from_orm(user)


@userRouter.put(
    "/editar",
    summary="Editar Perfil",
    description="Atualiza as informações visíveis no perfil do usuário. O atributo `foto` deve ser a string resultante de um arquivo em bytes codificado em base64. Caso o usuário opte por não escolher uma foto, o atributo deve ser nulo.",
    tags=[Tags.user]
)
def edit_user(perfil: UsuarioUpdate, access_token: str) -> Usuario:
    with get_session() as db:
        auth_controller = ControladorAuth(db)
        user = auth_controller.get_user(access_token)
        user = auth_controller.edit(access_token, perfil)

        return Usuario.from_orm(user)
