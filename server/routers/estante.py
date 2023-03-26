from fastapi import APIRouter, Depends
from typing import List, Annotated

from model.schema import Estante

import services.estante as estanteService


estanteRouter = APIRouter(
    prefix="/estante"
)


@estanteRouter.get("/")
def root():
    return {"info": "Wydra User API"}


# get estante do usuario
@estanteRouter.get("/getEstante", response_model=List[Estante])
def getEstante(idUsuario: int) -> List[Estante]:
    return estanteService.getEstanteUsuario(idUsuario)



# add obra na estante
@estanteRouter.post("/add")
def addEstante(estante: Estante) -> Estante:
    return estanteService.addEstante(estante)

# remove obra da estante
@estanteRouter.delete("/remover")
def removerObra(idUsuario: int, idObra: int) -> Estante:
    return estanteService.removerObra(idUsuario, idObra)

# altera estado da obra
@estanteRouter.put("/alterarEstado")
def alterarEstadoObra(idUsuario: int, idObra: int, estado: str) -> Estante:
    return estanteService.alterarEstadoObra(idUsuario, idObra, estado)
