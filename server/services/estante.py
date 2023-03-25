from model.schema import Estante

from controller.estante import ControladorEstante


def getEstanteUsuario(idUsuario: str) -> Estante:
    return ControladorEstante().getEstanteUsuario(idUsuario)


def addEstante(estante: str) -> Estante:
    return ControladorEstante().addEstante(estante)


def removeObra(idUsuario: str, idObra: str) -> Estante:
    return ControladorEstante().removeObra(idUsuario, idObra)


def alterarEstadoObra(idUsuario: str, idObra: str, estado: str) -> Estante:
    return ControladorEstante().alterarEstadoObra(idUsuario, idObra, estado)
