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
    tipo: TipoObra

    class Config:
        orm_mode = True

# Classe para obra com nota
class ObraNota(Obra):
    nota: float