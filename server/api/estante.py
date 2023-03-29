from fastapi import APIRouter
from typing import List

from controllers.estante import ControladorEstante
from app.schemas import Estante

estanteRouter = APIRouter(
    prefix="/estante"
)


# get estante do usuario
@estanteRouter.get("/getEstante", response_model=List[Estante])
def getEstante(idUsuario: int) -> List[Estante]:
    controlador_estante = ControladorEstante()
    return controlador_estante.getEstanteUsuario(idUsuario)


# add obra na estante
@estanteRouter.post("/add")
def addEstante(estante: Estante) -> Estante:
    controlador_estante = ControladorEstante()
    return controlador_estante.addEstante(estante)


# remove obra da estante
@estanteRouter.delete("/remover")
def removerObra(idUsuario: int, idObra: int) -> Estante:
    controlador_estante = ControladorEstante()
    return controlador_estante.removerObra(idUsuario, idObra)


# altera estado da obra
@estanteRouter.put("/alterarEstado")
def alterarEstadoObra(idUsuario: int, idObra: int, estado: str) -> Estante:
    controlador_estante = ControladorEstante()
    return controlador_estante.alterarEstadoObra(idUsuario, idObra, estado)
