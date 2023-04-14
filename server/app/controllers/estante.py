from datetime import datetime

from sqlalchemy.exc import IntegrityError

from core.exceptions import NotFoundException, BadRequestException

from app.models import ItemEstante as ormEstante
from app.schemas import ItemEstante, EstadoObra

from .obra import ControladorObra
from .usuario import ControladorUsuario


class ControladorEstante:
    def __init__(self, session):
        self.session = session
        self.obra_ctrl = ControladorObra(self.session)
        self.user_ctrl = ControladorUsuario(self.session)

    def get_by_user(self, idUsuario: int):
        estante = self.session.query(ormEstante).filter(
            ormEstante.id_usuario == idUsuario).all()

        return estante

    def get_obra_user(self, idUsuario: int, idObra: int):
        item = self.session.query(ormEstante).filter(
            ormEstante.id_usuario == idUsuario,
            ormEstante.id_obra == idObra).first()

        if not item:
            raise NotFoundException(detail="Obra não existe na estante.")

        return item

    def add(self, user, item: ItemEstante):

        if item.estado in [EstadoObra.finalizada, EstadoObra.abandonada]:
            data_inicio = datetime.now()
            data_fim = datetime.now()
        else:
            data_inicio = datetime.now()
            data_fim = None

        db_obra = self.obra_ctrl.get_or_create(item.obra.id)
        db_item = ormEstante(user, db_obra, item.estado,
                             data_inicio, data_fim)

        try:
            self.session.add(db_item)
            self.session.commit()
        except IntegrityError:
            raise BadRequestException(detail="Obra já existe na estante.")

        return db_item

    def remove_item(self, idUsuario: int, idObra: int):
        item = self.get_obra_user(idUsuario, idObra)
        res = ItemEstante.from_orm(item)

        self.session.delete(item)
        self.session.commit()

        return res

    def update_item(self, idUsuario: int, idObra: int, novoEstado: int):
        obra = self.get_obra_user(idUsuario, idObra)

        obra.estado = novoEstado

        if novoEstado in [EstadoObra.finalizada, EstadoObra.abandonada]:
            obra.data_fim = datetime.now()
        elif novoEstado == EstadoObra.em_progresso:
            obra.data_inicio = datetime.now()

        self.session.commit()

        return obra
