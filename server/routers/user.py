from fastapi import APIRouter

from domain import UserController
from domain import schemas

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.post("/signup", response_model=schemas.User)
def create_user(user : schemas.UserCreate):
    c = UserController()
    return c.create(user)

    return user

@userRouter.get("/{id}", response_model=schemas.User)
def get_user(id : int):
    c = UserController()
    user = c.get(id)

    return user

