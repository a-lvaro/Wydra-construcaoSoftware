from datetime import datetime

from app.models import ItemEstante
from app.schemas import ItemEstante as schemaEstante, EstadoObra, Usuario


class ControladorEstante:
    def __init__(self, session):
        self.session = session

    def getEstanteUsuario(self, idUsuario: int):
        return self.session.query(ItemEstante).filter(
            ItemEstante.id_usuario == idUsuario).all()

    def addItemEstante(self, usuario: Usuario, estante: schemaEstante):
        if estante.estado in [EstadoObra.finalizada, EstadoObra.abandonada]:
            data_inicio = datetime.now()
            data_fim = datetime.now()
        else:
            data_inicio = datetime.now()
            data_fim = None

        db_estante = ItemEstante(usuario, estante.id_obra,
                                 estante.tipo_obra, estante.estado,
                                 data_inicio, data_fim)

        self.session.add(db_estante)
        self.session.commit()
        self.session.refresh(db_estante)

        return estante

    def removerObra(self, idUsuario, idObra):
        obra = self.session.query(ItemEstante).filter(
            ItemEstante.id_usuario == idUsuario,
            ItemEstante.id_obra == idObra).first()

        self.session.delete(obra)
        self.session.commit()
        return obra

    def alterarEstadoObra(self, idUsuario, idObra, novoEstado):
        obra = self.session.query(ItemEstante).filter(
            ItemEstante.id_usuario == idUsuario, ItemEstante.id_obra == idObra
        ).first()

        obra.estado = novoEstado

        if novoEstado in [EstadoObra.finalizada, EstadoObra.abandonada]:
            obra.data_fim = datetime.now()
        elif novoEstado == 'Em progresso':
            obra.data_inicio = datetime.now()

        self.session.commit()
        self.session.refresh(obra)

        return obra
