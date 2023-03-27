from pydantic import BaseModel
from datetime import datetime


class Estante(BaseModel):
    id_usuario: int
    id_obra: int
    estado: str
    tipo: str

    class Config:
        orm_mode = True
