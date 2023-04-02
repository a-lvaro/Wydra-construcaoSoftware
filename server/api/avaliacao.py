from typing import List
from fastapi import APIRouter

from app.controllers import ControladorAuth
from app.controllers import ControladorAvaliacao

from app.schemas import Usuario, Avaliacao, AvaliacaoBase

from core.database import get_session

avaliacaoRouter = APIRouter(
    prefix="/avaliacao"
)

# add avaliação
@avaliacaoRouter.post("/add")
def add_avaliacao(token: str, avaliacao: AvaliacaoBase) -> AvaliacaoBase:
    db = get_session()

    controlador_avaliacao = ControladorAvaliacao(db)
    controlador_auth = ControladorAuth(db)

    user = controlador_auth.get_user(token)

    return controlador_avaliacao.create(user, avaliacao)


# get avaliações do usuario
@avaliacaoRouter.get("/user/{id}")
def get_user(id: int) -> List[AvaliacaoBase]:
    db = get_session()
    controlador_estante = ControladorAvaliacao(db)
    return controlador_estante.get_by_user(id)

# get avaliacoes da obra
@avaliacaoRouter.get("/obra/{id}")
def get_obra(id: int) -> List[Avaliacao]:
    db = get_session()
    controlador_estante = ControladorAvaliacao(db)
    return controlador_estante.get_by_obra(id)