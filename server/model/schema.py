from pydantic import BaseModel


class UsuarioBase(BaseModel):
    nome: str
    sobrenome: str
    nick: str


class UsuarioCreate(UsuarioBase):
    email: str
    senha: str
    senha_confirma: str


class Usuario(UsuarioBase):
    class Config:
        orm_mode = True
