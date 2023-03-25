from model.schema import Estante


def getEstanteUser(self, id) -> Estante:
    estante = self.session.query(Estante).filter(Estante.user_id == id)
    return estante


def addEstante(self, estante) -> Estante:
    self.session.add(estante)
    self.session.commit()
    return estante


def removeObra(self, idUsuario, idObra) -> Estante:
    obra = self.session.query(Estante).filter(
        Estante.user_id == idUsuario, Estante.obra_id == idObra)
    self.session.delete(obra)
    self.session.commit()
    return obra


def alterarEstadoObra(self, idUsuario, idObra, estado) -> Estante:
    obra = self.session.query(Estante).filter(
        Estante.user_id == idUsuario, Estante.obra_id == idObra)
    obra.estado = estado
    self.session.commit()
    return obra
