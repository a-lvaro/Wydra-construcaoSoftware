from pydantic import BaseModel
from datetime import datetime

class UsuarioBase(BaseModel):
    nome : str
    email : str

class UsuarioCreate(UsuarioBase):
    senha : str
    
    class Config:
        orm_mode = True

class Usuario(UsuarioBase):
    id : int
    data_cadastro : datetime

    class Config:
        orm_mode = True
