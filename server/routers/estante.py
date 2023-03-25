from fastapi import APIRouter, Depends
from typing import List, Annotated

from model.schema import Estante

import services.estante as estanteService


userRouter = APIRouter(
    prefix="/estante"
)


@userRouter.get("/")
def root():
    return {"info": "Wydra User API"}

# get estante de um usuario


@userRouter.getEstante("/{id}")
def getEstanteUser(idUsuario: int) -> Estante:
    return estanteService.getEstanteUsuario(idUsuario)


# add obra na estante
@userRouter.post("/add")
def addEstante(estante: Estante) -> Estante:
    return estanteService.addEstante(estante)

# remove obra da estante


@userRouter.delete("/remove")
def removeObra(idUsuario: int, idObra: int) -> Estante:
    return estanteService.removeObra(idUsuario, idObra)

# altera estado da obra


@userRouter.put("/alterarEstado")
def alterarEstadoObra(idUsuario: int, idObra: int, estado: str) -> Estante:
    return estanteService.alterarEstadoObra(idUsuario, idObra, estado)
