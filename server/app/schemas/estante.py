from pydantic import BaseModel, validator

from .obra import Obra, EstadoObra

# Item na estante referente a uma obra
class ItemEstante(BaseModel):
    obra: Obra
    estado: EstadoObra

    class Config:
        orm_mode = True