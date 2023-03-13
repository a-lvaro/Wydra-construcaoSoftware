from fastapi import APIRouter

from domain import ControladorUsuario
from domain import schemas

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.post("/signup")
def create_user(user : schemas.UsuarioCreate):
    c = ControladorUsuario()
    c.create(user)


@userRouter.get("/{id}", response_model=schemas.Usuario)
def get_user(id : int):
    c = ControladorUsuario()
    user = c.get(id)

    return user

