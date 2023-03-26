from model.schema import Estante
from model import schema

from controller.estante import ControladorEstante
from model.schema import Estante


def getEstanteUsuario(idUsuario: int) -> Estante:
    return ControladorEstante().getEstanteUsuario(idUsuario)


def addEstante(estante: Estante) -> Estante:
    return ControladorEstante().addEstante(estante)


def removerObra(idUsuario: int, idObra: int) -> Estante:
    return ControladorEstante().removerObra(idUsuario, idObra)


def alterarEstadoObra(idUsuario: int, idObra: int, estado: str) -> Estante:
    return ControladorEstante().alterarEstadoObra(idUsuario, idObra, estado)
