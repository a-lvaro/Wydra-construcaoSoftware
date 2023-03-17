from typing import ForwardRef
from typing import Union, List, Optional

from pydantic import BaseModel, validator


class UsuarioBase(BaseModel):
    nome: str


class UsuarioCreate(UsuarioBase):
    email: str
    senha: str

    class Config:
        orm_mode = True


def get_len(arg: Union[List | int]):
    if type(arg) == int:
        return arg
    else:
        return len(arg)


ListUsuario = ForwardRef("List[Usuario]")


class Usuario(UsuarioBase):
    id: int

    seguidores: Optional[int]
    _get_seguidores = validator(
        'seguidores', pre=True, allow_reuse=True)(get_len)

    seguindo: Optional[int]
    _get_seguindo = validator('seguindo', pre=True, allow_reuse=True)(get_len)

    class Config:
        orm_mode = True


Usuario.update_forward_refs()
