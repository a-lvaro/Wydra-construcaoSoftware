from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from bcrypt import checkpw

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
    token = services.user.autenticar(form_data.username, form_data.password)
    return token

@userRouter.post("/signup")
def sign_up(user: UsuarioCreate) -> Usuario:
    return services.user.cadastrar(user) 

@userRouter.get("/{id}")
def get_user(id: int) -> Usuario:
    db = Session()
    c = ControladorUsuario(db)
    user = c.get(id)

    return user


