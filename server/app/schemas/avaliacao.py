from pydantic import BaseModel, Field, constr
from typing import Optional

from .usuario import Usuario
from .obra import Obra, ObraNota


class AvaliacaoBase(BaseModel):
    nota: int = Field(ge=1, le=5)
    resenha: Optional[constr(min_length=0, max_length=1000)]

    class Config:
        orm_mode = True

# Classe para criar avaliações e resenhas
class AvaliacaoCreate(AvaliacaoBase):
    obra: Obra


# Classe avalliação para respostas
class Avaliacao(AvaliacaoBase):
    obra: ObraNota
    usuario: Usuario
    curtidas: int


