from typing import ForwardRef
from typing import Union, List, Optional

from pydantic import BaseModel, validator 
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

ListUsuario = ForwardRef("List[Usuario]")
class Usuario(UsuarioBase):
    id : int

    class Config:
        orm_mode = True

Usuario.update_forward_refs()

