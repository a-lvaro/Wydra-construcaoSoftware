from fastapi import APIRouter
from repositories import userRepository
from repositories.db import Session
from repositories.db import schemas

userRouter = APIRouter(
        prefix="/user"
    )

@userRouter.get("/{id}", response_model=schemas.User)
def get_user(id : int):
    db = Session()    
    return userRepository.get(db, id)
