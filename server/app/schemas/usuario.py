from fastapi import File
from pydantic import BaseModel, constr, validator
from pydantic import EmailStr
from typing import Optional, Annotated

class UsuarioBase(BaseModel):
    nome: str
    sobrenome: str
    email: EmailStr

    class Config:
        orm_mode = True

# Classe Usuário para cadastro
class UsuarioCreate(UsuarioBase):
    nick: constr(min_length=3, max_length=64)

    senha: constr(min_length=8, max_length=64)
    senha_confirma: constr(min_length=8, max_length=64)

    foto: Optional[Annotated[bytes, File()]]
    foto_ext: Optional[str] # tipo do arquivo ("jpg", "png")

# Classe Usuário para editar perfil
class UsuarioUpdate(UsuarioBase):
    nome: Optional[str]
    sobrenome: Optional[str]
    email: Optional[EmailStr]

    senha: Optional[constr(min_length=8, max_length=64)]
    senha_confirma: Optional[constr(min_length=8, max_length=64)]

    foto: Optional[Annotated[bytes, File()]]
    foto_ext: Optional[str] # tipo do arquivo ("jpg", "png")


# Retorna o número de seguidores da entidade
# Usuário do orm (número de elementos na lista seguidores)
def get_len(arg):
    if type(arg) == list:
        return len(arg)
    elif arg:
        return arg
    else:
        return 0


# Classe Usuário para respostas
class Usuario(UsuarioBase):
    nick: constr(min_length=3, max_length=64)

    caminho_foto: str
    id: int

    seguidores: Optional[int]
    _get_seguidores = validator(
        'seguidores', pre=True, allow_reuse=True)(get_len)

    seguindo: Optional[int]
    _get_seguindo = validator('seguindo', pre=True, allow_reuse=True)(get_len)

    class Config:
        orm_mode = True


# Classe Usuario para login
class UsuarioAuth(BaseModel):
    nick: constr(min_length=3, max_length=64)
    senha: constr(min_length=8, max_length=64)
