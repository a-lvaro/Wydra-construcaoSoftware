from typing import List
from fastapi import APIRouter

from app.controllers import ControladorAuth
from app.controllers import ControladorAvaliacao

from app.schemas import Avaliacao, AvaliacaoBase

from core.database import get_session

avaliacaoRouter = APIRouter(
    prefix="/avaliacao"
)


# add avaliação
@avaliacaoRouter.post("/add")
def add_avaliacao(token: str, avaliacao: AvaliacaoBase) -> AvaliacaoBase:
    with get_session() as db:
        controlador_avaliacao = ControladorAvaliacao(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_user(token)
        avaliacao = controlador_avaliacao.create(user, avaliacao)

        return AvaliacaoBase.from_orm(avaliacao)


# get avaliações do usuario
@avaliacaoRouter.get("/user/{id}")
def get_by_user(id: int) -> List[Avaliacao]:
    with get_session() as db:
        controlador_avaliacao = ControladorAvaliacao(db)
        avaliacoes = controlador_avaliacao.get_by_user(id)

        return [Avaliacao.from_orm(av) for av in avaliacoes]


# get avaliacoes da obra
@avaliacaoRouter.get("/obra/{id}")
def get_by_obra(id: int) -> List[Avaliacao]:
    with get_session() as db:
        controlador_avaliacao = ControladorAvaliacao(db)
        avaliacoes = controlador_avaliacao.get_by_obra(id)

        return [Avaliacao.from_orm(av) for av in avaliacoes]


# curtir avaliacao
@avaliacaoRouter.post("/curtir")
def curtir_avaliacao(token: str, idUsuario: int,
                     idObra: int, curtir: bool) -> Avaliacao:

    with get_session() as db:
        controlador_auth = ControladorAuth(db)
        controlador_auth.get_user(token)  # autentica o usuário

        controlador_avaliacao = ControladorAvaliacao(db)
        av = controlador_avaliacao.curtir(idUsuario, idObra, curtir)

        return Avaliacao.from_orm(av)
