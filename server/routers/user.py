from fastapi import APIRouter
from controller import userController

userRouter = APIRouter(
        prefix="/user"
        )

@userRouter.get("/{id}")
def get_user(id : int):
    c = userController()
    return c.get_user(id)
