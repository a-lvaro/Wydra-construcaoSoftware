from typing import ForwardRef, List

from pydantic import BaseModel, validator 
from datetime import datetime

class UsuarioBase(BaseModel):
    nome : str
    email : str

class UsuarioCreate(UsuarioBase):
    senha : str
    
    class Config:
        orm_mode = True

ListUsuario = ForwardRef("List[Usuario]")
class Usuario(UsuarioBase):
    id : int
    data_cadastro : datetime
    
    seguidores : int = 0
    _get_seguidores = validator('seguidores', pre=True, allow_reuse=True)(len)

    seguindo : int = 0
    _get_seguindo = validator('seguindo', pre=True, allow_reuse=True)(len)

    class Config:
        orm_mode = True

Usuario.update_forward_refs()
