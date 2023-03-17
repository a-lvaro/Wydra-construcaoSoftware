from pydantic import BaseModel, validator
from datetime import datetime
from pydantic import BaseModel
from typing import Union, List, Optional

<< << << < HEAD


class UsuarioBase(BaseModel):
    nome: str

    sobrenome: str
    nick: str


class UsuarioCreate(UsuarioBase):
    email: str
    senha: str
    senha_confirma: str


== == == =


class UsuarioBase(BaseModel):
    nome: str


class UsuarioCreate(UsuarioBase):
    email: str
    senha: str

    class Config:
        orm_mode = True


>>>>>> > main


def get_len(arg: Union[List | int]):
    if type(arg) == int:
        return arg
    else:
        return len(arg)


<< << << < HEAD
class Usuario(UsuarioBase):


== == == =

ListUsuario = ForwardRef("List[Usuario]")


class Usuario(UsuarioBase):
    id: int

    seguidores: Optional[int]
    _get_seguidores = validator(
        'seguidores', pre=True, allow_reuse=True)(get_len)

    seguindo: Optional[int]
    _get_seguindo = validator('seguindo', pre=True, allow_reuse=True)(get_len)


>>>>>> > main


class Config:
    orm_mode = True


Usuario.update_forward_refs()
