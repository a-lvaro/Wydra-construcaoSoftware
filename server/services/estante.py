from model import schemaEstante
from controller.estante import ControladorEstante


def getEstanteUsuario(idUsuario: int) -> schemaEstante:
    return ControladorEstante().getEstanteUsuario(idUsuario)


def addEstante(estante: schemaEstante) -> schemaEstante:
    return ControladorEstante().addEstante(estante)


def removerObra(idUsuario: int, idObra: int) -> schemaEstante:
    return ControladorEstante().removerObra(idUsuario, idObra)


def alterarEstadoObra(idUsuario: int, idObra: int, estado: str) -> schemaEstante:
    return ControladorEstante().alterarEstadoObra(idUsuario, idObra, estado)
