from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from bcrypt import checkpw

from controller import ControladorUsuario
from model.orm import Session

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


@userRouter.post("/login")
def log_in(form_data: OAuth2PasswordRequestForm = Depends()):

    # autentica o usuário pelo nick e senha e retorna um token de autenticação
    token = services.user.autenticar(form_data.username, form_data.password)
    return token


@userRouter.post("/signup")
def sign_up(user: UsuarioCreate) -> Usuario:
    return services.user.cadastrar(user)


@userRouter.get("/{nick}")
def get_user(nick: str) -> Usuario:
    db = Session()
    c = ControladorUsuario(db)

    user = c.get_by_nick(nick)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não existe.")

@userRouter.get("/me", response_model=Usuario)
async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = validar_token(token)
    return user
