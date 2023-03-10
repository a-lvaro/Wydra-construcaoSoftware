import hashlib
from sqlalchemy.orm import Session

from .db import *

class userRepository:
    @staticmethod
    def get(db : Session, id : int):
        return db.query(models.User).filter(models.User.id == id).first()

    @staticmethod
    def get_by_email(db : Session, email : str):
        return db.query(models.User).filter(models.User.email == email).first()

    @staticmethod
    def get_by_name(db : Session, name : str, skip : int = 0, limit : int = 100):
        return db.query(models.User).filter(name in models.User.name).offset(skip).limit(limit).all()

    @staticmethod
    def create_user(db : Session, user : schemas.UserCreate):
        hashed = hashlib.sha256(user.password.encode()).hexdigest()

        db_user = models.User(name=user.name, email=user.email, password=hashed)
        db.add(db_user)
        
        db.commit()
        db.refresh(db_user)

        return db_user

    def delete(db : Session, id : int):
        user = db.query(models.User).filter(models.User.id == id).first()
        
        if user:
            db.delete(user)
            db.commit()

