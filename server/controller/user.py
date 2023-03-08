from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
from fastapi import HTTPException

from services.database import engine
from model import User

class userController:
    def __init__(self):
        self.session = Session(engine)

    def get_user(self, id : int):
        user = self.session.get(User, id)

        if not user:
            raise HTTPException(status_code=404, detail="Usuário não existe")

        user_json = jsonable_encoder(user)
        del user_json["password"]

        return user_json

