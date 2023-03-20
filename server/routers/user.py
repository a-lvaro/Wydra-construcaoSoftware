from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import List

from controller import ControladorUsuario
from model.orm import Session

from model.schema import UsuarioCreate
from model.schema import Usuario
import services

userRouter = APIRouter(
    prefix="/user"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


@userRouter.post("/login")
def log_in(form_data: OAuth2PasswordRequestForm = Depends()):

    # autentica o usuário pelo nick e senha e retorna um token de autenticação
    token = services.user.autenticar(form_data.username, form_data.password)
    return token


@userRouter.post("/signup")
def sign_up(user: UsuarioCreate) -> Usuario:
    return services.user.cadastrar(user)


@userRouter.get("/search")
def search_user(nick: str) -> List[Usuario]:
    db = Session()
    c = ControladorUsuario(db)

    results = c.search_by_nick(nick)
    return results


@userRouter.get("/{nick}")
def get_user(nick: str) -> Usuario:
    db = Session()
    c = ControladorUsuario(db)

    user = c.get_by_nick(nick)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não existe.")

    return user
