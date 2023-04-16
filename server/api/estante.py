from fastapi import APIRouter
from typing import List

from core.database import get_session
from app.controllers import ControladorEstante, ControladorAuth
from app.schemas import ItemEstante, EstadoObra, ItemEstanteCreate

estanteRouter = APIRouter(
    prefix="/estante"
)


# add obra na estante
@estanteRouter.post("/add")
def add_item(access_token: str, item: ItemEstanteCreate) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_by_token(access_token)
        item = controlador_estante.add(user, item)

        return ItemEstante.from_orm(item)


# remove obra da estante
@estanteRouter.delete("/remover")
def remove_item(token: str, idObra: int) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_user(token)
        item = controlador_estante.remove_item(user.id, idObra)

        return item


# altera estado da obra
@estanteRouter.put("/alterar", response_model=ItemEstante)
def update_item(access_token: str, idObra: int, estado: EstadoObra):
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_by_token(access_token)
        item = controlador_estante.update_item(user.id, idObra, estado)

        return ItemEstante.from_orm(item)


# get estante do usuario
@estanteRouter.get("/{id}")
def get_by_user(id: int) -> List[ItemEstante]:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        estante = controlador_estante.get_by_user(id)

        return [ItemEstante.from_orm(item) for item in estante]


# get obra do usuario
@estanteRouter.get("/{id_user}/{id_obra}")
def get_obra_user(id_user: int, id_obra: int) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        obra = controlador_estante.get_obra_user(id_user, id_obra)

        return ItemEstante.from_orm(obra)
