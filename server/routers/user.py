from fastapi import APIRouter

from domain import ControladorUsuario
from domain import schemas

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.post("/signup", response_model=schemas.Usuario)
def create_user(user : schemas.UsuarioCreate):
    c = ControladorUsuario()
    return c.create(user)

    return user

@userRouter.get("/{id}", response_model=schemas.Usuario)
def get_user(id : int):
    c = ControladorUsuario()
    user = c.get(id)

    return user

