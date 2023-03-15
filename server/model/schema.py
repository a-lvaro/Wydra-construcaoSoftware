from typing import Union, List, Optional

from pydantic import BaseModel
from datetime import datetime

class UsuarioBase(BaseModel):
    nome : str
    sobrenome : str
    nick : str

class UsuarioCreate(UsuarioBase):
    email : str
    senha : str
    senha_confirma : str
    

def get_len(arg : Union[List|int]):
    if type(arg) == int:
        return arg
    else:
        return len(arg)

class Usuario(UsuarioBase):

    class Config:
        orm_mode = True


