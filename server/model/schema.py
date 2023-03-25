from typing import Union, List, Optional

from pydantic import BaseModel
from datetime import datetime


class UsuarioBase(BaseModel):
    nome: str
    sobrenome: str
    nick: str


# Classe Usuário para cadastro
class UsuarioCreate(UsuarioBase):
    email: str
    senha: str
    senha_confirma: str


# Retorna o número de seguidores da entidade
# Usuário do orm (número de elementos na lista seguidores)
def get_len(arg):
    # retorna None se a lista for vazia
    if type(arg) == list:
        return len(arg)
    elif arg:
        return arg
    else:
        return len(arg)


# Classe Usuário para respostas
class Usuario(UsuarioBase):

    class Config:
        orm_mode = True
