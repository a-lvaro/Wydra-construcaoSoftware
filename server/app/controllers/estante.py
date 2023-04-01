from datetime import datetime

from core.database import get_session
from app.schemas.estante import Estante
from app.models.estante import Estante as ormEstante


class ControladorEstante:
    def __init__(self):
        self.session = get_session()

    def getEstanteUsuario(self, idUsuario: int) -> Estante:
        return self.session.query(ormEstante).filter(ormEstante.id_usuario == idUsuario).all()

    def addEstante(self, estante: Estante) -> Estante:
        db_estante = ormEstante()

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
        obra = self.session.query(ormEstante).filter(
            ormEstante.id_usuario == idUsuario,
            ormEstante.id_obra == idObra).one()
        self.session.delete(obra)
        self.session.commit()
        return obra

    def alterarEstadoObra(self, idUsuario, idObra, novoEstado):
        obra = self.session.query(ormEstante).filter(
            ormEstante.id_usuario == idUsuario, ormEstante.id_obra == idObra).one()
        obra.estado = novoEstado

        if novoEstado in ['Finalizada', 'Abandonada']:
            obra.data_fim = datetime.now()
        elif novoEstado == 'Em progresso':
            obra.data_inicio = datetime.now()

        self.session.commit()
        self.session.refresh(obra)
        return obra
