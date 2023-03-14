from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from bcrypt import checkpw

from controller import ControladorUsuario
from model.schema import UsuarioCreate
from model.schema import Usuario

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.post("/signup")
def sign_up(user: UsuarioCreate) -> Usuario:
    c = ControladorUsuario()
    new_user = c.create(user)

    return new_user


@userRouter.get("/{id}")
def get_user(id: int) -> Usuario:
    c = ControladorUsuario()
    user = c.get(id)

    return user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@userRouter.post("/login")
def log_in(form_data: OAuth2PasswordRequestForm = Depends()):
    c = ControladorUsuario()
    user = c.get_by_email(form_data.username)

    if user and checkpw(form_data.password.encode('utf-8'), user.senha.encode('utf-8')):
        return {"access_token": user.email, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos.")
