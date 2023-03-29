from pydantic import BaseModel

# Classe genérica para obra
class Obra(BaseModel):
    id: int
    titulo: str
    descricao: str
    autor: str | None

    class Config:
        orm_mode = True


# Classe Filme para respostas
class Filme(Obra):
    pass
