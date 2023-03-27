from fastapi import HTTPException
from sqlalchemy.exc import DBAPIError

from typing import List
from datetime import datetime, timedelta

from fastapi.security import OAuth2PasswordBearer
from bcrypt import hashpw, gensalt, checkpw
from jose import JWTError, jwt

from app.controllers.usuario import Controlador as ControladorUsuario

from core.database import Session
from app.schemas.usuario import UsuarioCreate
from app.schemas.usuario import Usuario

# TODO:
# - Organizar esse código (talvez dividir em outros módulos)


SECRET_KEY = "secret"  # por enquanto
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# Autenticação do Usuário
def autenticar(nick, senha):
    db = Session()
    ctrl = ControladorUsuario(db)

    db_user = ctrl.get_by_nick(nick)

    if db_user and checkpw(senha.encode(), db_user.senha.encode()):
        user = Usuario.from_orm(db_user)
        token = create_token(user)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=400,
            detail="Email ou senha incorretos."
        )


# Cadastra um novo usuário
def cadastrar(user: UsuarioCreate) -> Usuario:
    db = Session()
    ctrl = ControladorUsuario(db)

    # TODO:
    # - Validar email (middleware?)

    # validação do cadastro
    if user.senha != user.senha_confirma:
        raise HTTPException(status_code=400, detail="Senhas inválidas.")
    if not (user.nome and user.sobrenome and
            user.nick and user.email and user.senha):
        raise HTTPException(status_code=400, detail="Atributos inválidos.")

    # password hashing
    user.senha = hashpw(user.senha.encode(), gensalt()).decode()

    try:
        new_user = ctrl.create(user)
    except DBAPIError:
        # erro de integridade no db (nick ou email já cadastrado)
        raise HTTPException(status_code=400, detail="Usuário já cadastrado.")

    return Usuario.from_orm(new_user)


# Retorna a entidade Usuário a partir de seu nick
def get_user_by_nick(nick: str) -> Usuario:
    db = Session()
    ctrl = ControladorUsuario(db)

    user = ctrl.get_by_nick(nick)

    if not user:
        raise HTTPException(status_code=404, detail="Usuário não existe")

    return user


# Retorna uma lista de usuários cujo nick contém determinada string
def search_user_by_nick(nick: str) -> List[Usuario]:
    db = Session()
    ctrl = ControladorUsuario(db)

    results = ctrl.search_by_nick(nick)
    return results


# Cria um novo token de autenticação para o usuário
def create_token(user: Usuario, expires_delta: timedelta | None = None) -> str:
    to_encode = user.dict()

    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=60)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY)

    return encoded_jwt


# Decodifica o token e retorna o seu usuário
def validar_token(token: str) -> Usuario:
    credentials_exception = HTTPException(
        status_code=401,
        detail="Credenciais inválidas.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, SECRET_KEY)
        nick: str = payload.get("nick")

        if nick is None:
            raise credentials_exception

    except JWTError:
        raise credentials_exception

    db = Session()
    ctrl = ControladorUsuario(db)
    user = ctrl.get_by_nick(nick)

    if user is None:
        raise credentials_exception

    return user
