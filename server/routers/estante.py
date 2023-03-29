from fastapi import APIRouter
from model import schemaEstante
from typing import List
import services.estante as estanteService


estanteRouter = APIRouter(
    prefix="/estante"
)


@estanteRouter.get("/")
def root():
    return {"info": "Wydra User API"}


# get estante do usuario
@estanteRouter.get("/getEstante", response_model=List[schemaEstante.Estante])
def getEstante(idUsuario: int) -> List[schemaEstante.Estante]:
    return estanteService.getEstanteUsuario(idUsuario)

# add obra na estante


@estanteRouter.post("/add")
def addEstante(estante: schemaEstante.Estante) -> schemaEstante.Estante:
    return estanteService.addEstante(estante)

# remove obra da estante


@estanteRouter.delete("/remover")
def removerObra(idUsuario: int, idObra: int) -> schemaEstante.Estante:
    return estanteService.removerObra(idUsuario, idObra)

# altera estado da obra


@estanteRouter.put("/alterarEstado")
def alterarEstadoObra(idUsuario: int, idObra: int, estado: str) -> schemaEstante.Estante:
    return estanteService.alterarEstadoObra(idUsuario, idObra, estado)
