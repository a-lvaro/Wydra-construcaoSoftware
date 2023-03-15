from fastapi import HTTPException 
from bcrypt import hashpw, gensalt, checkpw
from sqlalchemy.exc import DBAPIError

from controller import ControladorUsuario

from model.orm import Session
from model.schema import UsuarioCreate
from model.schema import Usuario

# Autenticação do Usuário
def autenticar(email, senha):
    db = Session()
    ctrl = ControladorUsuario(db)

    user = ctrl.get_by_email(email)

    if user and checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
        return {"acces_token": user.email, "token_type": "bearer"}
    else:
        raise HTTPException(status_code=400, detail="Email ou senha incorretos.")

    # TODO:
    # - Usar tokens seguros

# Cadastra um novo usuário
def cadastrar(user : UsuarioCreate) -> Usuario:
    db = Session()
    ctrl = ControladorUsuario(db)

    # TODO:
    # - Validar email (middleware?)

    # validação do cadastro
    if user.senha != user.senha_confirma:
        raise HTTPException(status_code=400, detail="Senhas inválidas.")
    if not (user.nome and user.sobrenome and user.nick and user.email and user.senha):
        raise HTTPException(status_code=400, detail="Atributos inválidos.")

    # password hashing
    user.senha = hashpw(user.senha.encode('utf-8'), gensalt()).decode('utf-8')

    try:
        new_user = ctrl.create(user)
    except DBAPIError: # erro de integridade no db (nick ou email já cadastrado)
        raise HTTPException(status_code=400, detail="Usuário já cadastrado.")

    return Usuario.from_orm(new_user)
