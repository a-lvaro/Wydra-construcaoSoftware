from pydantic import BaseModel, Field, constr
from typing import Optional

from .usuario import Usuario
from .obra import Obra

class AvaliacaoBase(BaseModel):
    nota: int = Field(ge=1, le=5)
    resenha: Optional[constr(min_length=100, max_length=1000)]
    obra: Obra

    class Config:
        orm_mode = True

# Classe para criar avaliações e resenhas
class Avaliacao(AvaliacaoBase):
    usuario: Usuario
