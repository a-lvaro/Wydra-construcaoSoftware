from fastapi import APIRouter
from typing import List

from core.database import get_session
from core.config import Tags

from app.controllers import ControladorEstante, ControladorAuth
from app.schemas import ItemEstante, EstadoObra, ItemEstanteCreate

estanteRouter = APIRouter(
    prefix="/estante"
)

@estanteRouter.post(
    "/add",
    summary="Adicionar Obra na Estante",
    description="Adiciona uma obra na estante do usuário.",
    tags=[Tags.estante])
def add_item(access_token: str, item: ItemEstanteCreate) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_by_token(access_token)
        item = controlador_estante.add(user, item)

        return ItemEstante.from_orm(item)

@estanteRouter.delete(
    "/remover",
    summary="Remover Obra da Estante",
    description="Remove a obra de id `obra.id` da estante do usuário.",
    tags=[Tags.estante])
def remove_item(token: str, idObra: int) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_user(token)
        item = controlador_estante.remove_item(user.id, idObra)

        return item

@estanteRouter.put(
    "/alterar", 
    response_model=ItemEstante,
    summary="Alterar Estado de uma Obra na Estante",
    description="""
Altera o estado da obra `obra.id`. O parâmetro `estado` é um enum com os seguintes valores:
|Estado|Valor|
|------|-----|
|Lista de Desejos|1|
|Em progresso|2|
|Finalizada|3|
|Abandonada|4|
""",
    tags=[Tags.estante])
def update_item(access_token: str, idObra: int, estado: EstadoObra):
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_by_token(access_token)
        item = controlador_estante.update_item(user.id, idObra, estado)

        return ItemEstante.from_orm(item)


@estanteRouter.get(
    "/{id}",
    summary="Obter estante do usuário",
    description="Obtem uma lista de todas as obras na estante do usuário identificado por `id`.",
    tags=[Tags.estante])
def get_by_user(id: int) -> List[ItemEstante]:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        estante = controlador_estante.get_by_user(id)

        return [ItemEstante.from_orm(item) for item in estante]
