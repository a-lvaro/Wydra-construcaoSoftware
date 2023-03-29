from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Estante(BaseModel):
    id_usuario: int
    id_obra: int
    estado: str
    tipo: str
    data_inicio: datetime
    data_fim: Optional[datetime]

    class Config:
        orm_mode = True
