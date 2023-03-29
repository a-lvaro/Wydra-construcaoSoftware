from pydantic import BaseModel
from typing import Optional, Enum

class TipoObra(Enum):
    Filme = "filme"
    Livro = "livro"

# Classe genérica para obra
class Obra(BaseModel):
    id: int
    titulo: str
    descricao: str
    autor: Optional[str]
    tipo: Optional[TipoObra]

    class Config:
        orm_mode = True

# Classe Filme para respostas
class Filme(Obra):
    tipo = TipoObra.Filme
