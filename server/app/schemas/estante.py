from pydantic import BaseModel, validator
from enum import IntEnum


class EstadoObra(IntEnum):
    lista_de_desejos = 1
    em_progresso = 2
    finalizada = 3
    abandonada = 4


class TipoObra(IntEnum):
    filme = 1


# Classe genérica para obra
class Obra(BaseModel):
    id: int
    nota: float
    tipo: TipoObra


class ItemEstante(BaseModel):
    id_usuario: int
    id_obra: int

    tipo: TipoObra
    estado: EstadoObra

    class Config:
        orm_mode = True
