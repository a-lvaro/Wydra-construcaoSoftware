from pydantic import BaseModel, constr, validator
from pydantic import EmailStr, Field
from typing import Optional


class UsuarioBase(BaseModel):
    nome: str
    sobrenome: str
    nick: constr(min_length=3, max_length=64)


# Classe Usuário para cadastro
class UsuarioCreate(UsuarioBase):
    email: EmailStr
    senha: constr(min_length=8, max_length=64)
    senha_confirma: constr(min_length=8, max_length=64)


# Retorna o número de seguidores da entidade
# Usuário do orm (número de elementos na lista seguidores)
def get_len(arg):
    # retorna None se a lista for vazia
    if type(arg) == list:
        return len(arg)
    elif arg:
        return arg
    else:
        return 0


# Classe Usuário para respostas
class Usuario(UsuarioBase):
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


# Classe para configurar o perfil
class Perfil(UsuarioBase):
    email: str

    class Config:
        orm_mode = True


# Classe para avaliações e resenhas
class Avaliacao(BaseModel):
    nota: int = Field(ge=1, le=5)
    id_obra: int
    usuario: Usuario
    resenha: Optional[constr(min_length=100, max_length=1000)]
