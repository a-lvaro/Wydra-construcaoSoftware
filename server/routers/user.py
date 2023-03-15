from fastapi import APIRouter

from controller import ControladorUsuario
from model.schemas import UsuarioCreate
from model.schemas import Usuario

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.post("/signup")
def create_user(user : UsuarioCreate):
    c = ControladorUsuario()
    c.create(user)


@userRouter.get("/{id}", response_model = Usuario)
def get_user(id : int):
    c = ControladorUsuario()
    user = c.get(id)

    return user

