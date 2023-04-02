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
def add_obra(estante: ItemEstante) -> ItemEstante:
    db = get_session()

    controlador_estante = ControladorEstante(db)
    controlador_auth = ControladorAuth(db)

    user = controlador_auth.get(estante.id_usuario)

    return controlador_estante.addItemEstante(user, estante)


# remove obra da estante
@estanteRouter.delete("/remover")
def remover_obra(idUsuario: int, idObra: int) -> ItemEstante:
    db = get_session()
    controlador_estante = ControladorEstante(db)
    return controlador_estante.removerObra(idUsuario, idObra)


# altera estado da obra
@estanteRouter.put("/alterar", response_model=ItemEstante)
def alterar_estado(idUsuario: int, idObra: int, estado: EstadoObra):
    db = get_session()
    controlador_estante = ControladorEstante(db)

    return controlador_estante.alterarEstadoObra(idUsuario, idObra, estado)


# get estante do usuario
@estanteRouter.get("/{id}")
def get_estante(id: int) -> List[ItemEstante]:
    db = get_session()
    controlador_estante = ControladorEstante(db)
    return controlador_estante.getEstanteUsuario(id)
