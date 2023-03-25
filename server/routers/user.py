from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from typing import List, Annotated

from model.schema import UsuarioCreate
from model.schema import Usuario

from services.user import oauth2_scheme
from services.user import autenticar, cadastrar, validar_token
from services.user import get_user_by_nick, search_user_by_nick


userRouter = APIRouter(
    prefix="/user"
)


@userRouter.get("/")
def root():
    return {"info": "Wydra User API"}


@userRouter.get("/me", response_model=Usuario)
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = validar_token(token)
    return user


@userRouter.post("/login")
def log_in(form_data: OAuth2PasswordRequestForm = Depends()):
    # autentica o usuário pelo nick e senha e retorna um token de autenticação
    token = autenticar(form_data.username, form_data.password)
    return token


@userRouter.post("/signup")
def sign_up(user: UsuarioCreate) -> Usuario:
    new_user = cadastrar(user)
    return new_user


@userRouter.get("/search")
def search_user(nick: str) -> List[Usuario]:
    results = search_user_by_nick(nick)
    return results


@userRouter.get("/{nick}")
def get_user(nick: str) -> Usuario:
    user = get_user_by_nick()
    return user
