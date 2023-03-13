from fastapi import APIRouter

from controller import ControladorUsuario
from model.schema import UsuarioCreate
from model.schema import Usuario

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.post("/signup")
def create_user(user: UsuarioCreate) -> Usuario:
    c = ControladorUsuario()
    new_user = c.create(user)

    return new_user


@userRouter.get("/{id}")
def get_user(id: int) -> Usuario:
    c = ControladorUsuario()
    user = c.get(id)

    return user

