from typing import List
from fastapi import APIRouter

from app.controllers import ControladorAuth
from app.controllers import ControladorAvaliacao

from app.schemas import Avaliacao, AvaliacaoCreate

from core.database import get_session
from core.config import Tags

avaliacaoRouter = APIRouter(
    prefix="/avaliacao",
)

@avaliacaoRouter.post(
    "/add", 
    summary="Criar avaliação",
    description="Cria uma nova avaliação para a obra com o id `obra.id` e tipo `obra.tipo`. O atributo `nota` varia de 1 a 5.",
    tags=[Tags.avaliacao])
def add_avaliacao(token: str, avaliacao: AvaliacaoCreate) -> AvaliacaoCreate:
    with get_session() as db:
        controlador_avaliacao = ControladorAvaliacao(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_user(token)
        avaliacao = controlador_avaliacao.create(user, avaliacao)

        return AvaliacaoCreate.from_orm(avaliacao)

@avaliacaoRouter.get(
    "/user/{id}",
    summary="Obter avaliações do usuário",
    description="Obtem uma lista de todas as avaliações feitas pelo usuário identificado por `id`.",
    tags=[Tags.avaliacao])
def get_by_user(id: int) -> List[Avaliacao]:
    with get_session() as db:
        controlador_avaliacao = ControladorAvaliacao(db)
        avaliacoes = controlador_avaliacao.get_by_user(id)

        return [Avaliacao.from_orm(av) for av in avaliacoes]

@avaliacaoRouter.get(
    "/obra/{id}",
    summary="Obter avaliações da obra",
    description="Obtem uma lista de todas as avaliações da obra identificada por `id`.",
    tags=[Tags.avaliacao])
def get_by_obra(id: int) -> List[Avaliacao]:
    with get_session() as db:
        controlador_avaliacao = ControladorAvaliacao(db)
        avaliacoes = controlador_avaliacao.get_by_obra(id)

        return [Avaliacao.from_orm(av) for av in avaliacoes]


@avaliacaoRouter.post(
    "/curtir",
    summary="Curtir avaliação",
    description="Atualiza o contador de curtidas da avaliação. O atributo `curtida` pode ser `true`, adicionando uma curtida, ou `false`, subtraindo uma curtida.",
    tags=[Tags.avaliacao])
def curtir_avaliacao(token: str, idUsuario: int,
                     idObra: int, curtir: bool) -> Avaliacao:

    with get_session() as db:
        controlador_auth = ControladorAuth(db)
        controlador_auth.get_user(token)  # autentica o usuário

        controlador_avaliacao = ControladorAvaliacao(db)
        av = controlador_avaliacao.curtir(idUsuario, idObra, curtir)

        return Avaliacao.from_orm(av)
