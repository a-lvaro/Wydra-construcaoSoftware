from fastapi import APIRouter
from fastapi import HTTPException

from repositories import userRepository
from repositories.db import Session
from repositories.db import schemas

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.get("/{id}", response_model=schemas.User)
def get_user(id : int):
    db = Session()   
    user = userRepository.get(db, id)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não existe")

    return user
