from model.schema import Estante
from model import schema

from controller.estante import ControladorEstante
from model.schema import Estante


def getEstanteUsuario(idUsuario: str) -> Estante:
    return ControladorEstante().getEstanteUsuario(idUsuario)


def addEstante(estante: Estante) -> Estante:
    return ControladorEstante().addEstante(estante)


def removeObra(idUsuario: str, idObra: str) -> Estante:
    return ControladorEstante().removeObra(idUsuario, idObra)


def alterarEstadoObra(idUsuario: str, idObra: str, estado: str) -> Estante:
    return ControladorEstante().alterarEstadoObra(idUsuario, idObra, estado)
