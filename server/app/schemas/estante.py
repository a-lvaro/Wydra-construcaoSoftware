from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .obra import Obra, EstadoObra


# Item na estante referente a uma obra
class ItemEstante(BaseModel):
    obra: Obra
    estado: EstadoObra

    class Config:
        orm_mode = True


class ItemEstanteData(ItemEstante):
    data_inicio: Optional[datetime]
    data_fim: Optional[datetime]
