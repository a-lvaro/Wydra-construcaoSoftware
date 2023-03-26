from model.orm import Session
from model import orm

from model.schema import Estante

from datetime import datetime


class ControladorEstante:
    def __init__(self):
        self.session = Session()

    def getEstanteUsuario(self, idUsuario: int) -> Estante:
        return self.session.query(orm.Estante).filter(orm.Estante.id_usuario == idUsuario).all()

    def addEstante(self, estante: Estante) -> Estante:
        db_estante = orm.Estante()

        db_estante.id_usuario = estante.id_usuario
        db_estante.id_obra = estante.id_obra
        db_estante.estado = estante.estado
        db_estante.tipo = estante.tipo

        if estante.estado in ['Finalizada', 'Abandonada']:
            db_estante.data_inicio = datetime.now()
            db_estante.data_fim = datetime.now()
        else:
            db_estante.data_inicio = datetime.now()
            db_estante.data_fim = None

        self.session.add(db_estante)
        self.session.commit()
        self.session.refresh(db_estante)

        return estante

    def removerObra(self, idUsuario, idObra):
        obra = self.session.query(orm.Estante).filter(
            orm.Estante.id_usuario == idUsuario,
            orm.Estante.id_obra == idObra).one()
        self.session.delete(obra)
        self.session.commit()
        return obra

    def alterarEstadoObra(self, idUsuario, idObra, novoEstado):
        obra = self.session.query(orm.Estante).filter(
            orm.Estante.id_usuario == idUsuario, orm.Estante.id_obra == idObra).one()
        obra.estado = novoEstado

        if novoEstado in ['Finalizada', 'Abandonada']:
            obra.data_fim = datetime.now()
        elif novoEstado == 'Em progresso':
            obra.data_inicio = datetime.now()

        self.session.commit()
        self.session.refresh(obra)
        return obra
