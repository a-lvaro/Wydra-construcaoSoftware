from pydantic import BaseModel
from datetime import datetime


class Estante(BaseModel):
    id_usuario: int
    id_obra: int
    estado: str
    data_inicio: datetime
    data_fim: Optional[datetime]

    class Config:
        orm_mode = True
