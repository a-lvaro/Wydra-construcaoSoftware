from model.orm import Session
from model.schema import Estante


class ControladorEstante:
    def __init__(self):
        self.estante = Estante()
        self.session = Session()

    def getEstanteUsuario(self, id):
        estante = self.session.query(Estante).filter(Estante.idUsuario == id)
        return estante

    def addEstante(self, estante):
        self.session.add(estante)
        self.session.commit()
        return estante

    def removeObra(self, idUsuario, idObra):
        obra = self.session.query(Estante).filter(
            Estante.idUsuario == idUsuario, Estante.idObra == idObra)
        self.session.delete(obra)
        self.session.commit()
        return obra

    def alterarEstadoObra(self, idUsuario, idObra, estado):
        obra = self.session.query(Estante).filter(
            Estante.idUsuario == idUsuario, Estante.idObra == idObra)
        obra.estado = estado
        self.session.commit()
        return obra
