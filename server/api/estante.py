from fastapi import APIRouter
from typing import List

from core.database import get_session
from app.controllers import ControladorEstante, ControladorAuth
from app.schemas import ItemEstante, EstadoObra

estanteRouter = APIRouter(
    prefix="/estante"
)


# add obra na estante
@estanteRouter.post("/add")
def add_item(access_token: str, estante: ItemEstante) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_by_token(access_token)

        return controlador_estante.add(user, estante)


# remove obra da estante
@estanteRouter.delete("/remover")
def remove_item(token: str, idObra: int) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_user(token)

        return controlador_estante.remove_item(user.id, idObra)


# altera estado da obra
@estanteRouter.put("/alterar", response_model=ItemEstante)
def update_item(access_token: str, idObra: int, estado: EstadoObra):
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        controlador_auth = ControladorAuth(db)

        user = controlador_auth.get_by_token(access_token)

        return controlador_estante.update_item(user.id, idObra, estado)


# get estante do usuario
@estanteRouter.get("/{id}")
def get_by_user(id: int) -> List[ItemEstante]:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        return controlador_estante.get_by_user(id)


# get obra do usuario
@estanteRouter.get("/{id_user}/{id_obra}")
def get_obra_user(id_user: int, id_obra: int) -> ItemEstante:
    with get_session() as db:
        controlador_estante = ControladorEstante(db)
        return controlador_estante.get_obra_user(id_user, id_obra)
