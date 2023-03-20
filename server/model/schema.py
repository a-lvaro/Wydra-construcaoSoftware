from pydantic import BaseModel, validator
from typing import List


class UsuarioBase(BaseModel):
    nome: str
    sobrenome: str
    nick: str


class UsuarioCreate(UsuarioBase):
    email: str
    senha: str
    senha_confirma: str


# Retorna o número de seguidores da entidade
# Usuário do orm (número de elementos na lista seguidores)
def get_len(arg):
    # retorna None se a lista for vazia
    if type(arg) == list:
        return len(arg) if arg else None
    else:
        return arg


class Usuario(UsuarioBase):
    id: int

    seguidores: int
    _get_seguidores = validator(
        'seguidores', pre=True, allow_reuse=True)(get_len)

    seguindo: int
    _get_seguindo = validator('seguindo', pre=True, allow_reuse=True)(get_len)

    class Config:
        orm_mode = True


class Elenco(BaseModel):
    nome: str
    papel: str


class Filme(BaseModel):
    id: int
    titulo: str
    descricao: str
    diretor: str
    duracao: int  # Duração em minutos
    generos: List[str]
    elenco: List[Elenco]

    class Config:
        orm_mode = True
