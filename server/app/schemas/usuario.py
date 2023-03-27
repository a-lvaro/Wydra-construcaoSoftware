from pydantic import BaseModel, validator

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
        return 0


# Classe Usuário para respostas
class Usuario(UsuarioBase):
    id: int

    seguidores: int
    _get_seguidores = validator(
        'seguidores', pre=True, allow_reuse=True)(get_len)

    seguindo: int
    _get_seguindo = validator('seguindo', pre=True, allow_reuse=True)(get_len)

    class Config:
        orm_mode = True