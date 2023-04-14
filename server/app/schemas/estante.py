from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .obra import ObraNota, EstadoObra


# Item na estante referente a uma obra
class ItemEstante(BaseModel):
    obra: ObraNota
    estado: EstadoObra

    class Config:
        orm_mode = True


class ItemEstanteData(ItemEstante):
    data_inicio: Optional[datetime]
    data_fim: Optional[datetime]
