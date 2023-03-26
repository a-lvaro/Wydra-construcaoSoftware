from model.orm import Session
from model import orm
from model import schema

from model.schema import Estante

from datetime import datetime


class ControladorEstante:
    def __init__(self):
        self.session = Session()

    def getEstanteUsuario(self, idUsuario :str) -> schema.Estante:
        return self.session.query(orm.Estante).filter(orm.Estante.id_usuario == idUsuario).all()

    # TODO tratar exceções
    def addEstante(self, estante :Estante) -> schema.Estante:
        db_estante = orm.Estante()

        db_estante.id_usuario = estante.id_usuario
        db_estante.id_obra = estante.id_obra
        db_estante.estado = estante.estado
        db_estante.tipo = estante.tipo
        db_estante.data_inicio = datetime.utcnow()
        db_estante.data_fim = datetime.utcnow()


        self.session.add(db_estante)
        self.session.commit()
        self.session.refresh(db_estante)

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
