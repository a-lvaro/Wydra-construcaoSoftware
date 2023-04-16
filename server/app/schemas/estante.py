from pydantic import BaseModel
from datetime import datetime
from typing import Optional

from .obra import Obra, ObraNota, EstadoObra


# Item na estante referente a uma obra
class ItemEstanteBase(BaseModel):
    estado: EstadoObra

    class Config:
        orm_mode = True

class ItemEstanteCreate(ItemEstanteBase):
    obra: Obra

class ItemEstante(ItemEstanteBase):
    obra: Obra
    data_inicio: Optional[datetime]
    data_fim: Optional[datetime]
