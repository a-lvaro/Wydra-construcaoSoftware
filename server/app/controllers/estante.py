from datetime import datetime
from typing import List

from sqlalchemy.exc import NoResultFound, IntegrityError

from core.exceptions import NotFoundException, BadRequestException

from app.models import ItemEstante
from app.schemas import ItemEstante as schemaEstante, EstadoObra

from .obra import ControladorObra
from .usuario import ControladorUsuario


class ControladorEstante:
    def __init__(self, session):
        self.session = session
        self.obra_ctrl = ControladorObra(self.session)
        self.user_ctrl = ControladorUsuario(self.session)

    def get_by_user(self, idUsuario: int) -> List[schemaEstante]:
        user = self.user_ctrl.get(idUsuario)
        return user.estante

    def get_obra_user(self, idUsuario: int, idObra: int) -> schemaEstante:
        try:
            item = self.session.query(ItemEstante).filter(
                ItemEstante.id_usuario == idUsuario,
                ItemEstante.id_obra == idObra).one()

            return item
        except NoResultFound:
            raise NotFoundException(detail="Obra não existe na estante.")

    def add(self, user: int, estante: schemaEstante) -> schemaEstante:
        if estante.estado in [EstadoObra.finalizada, EstadoObra.abandonada]:
            data_inicio = datetime.now()
            data_fim = datetime.now()
        else:
            data_inicio = datetime.now()
            data_fim = None

        db_obra = self.obra_ctrl.get(estante.obra.id)
        db_estante = ItemEstante(user, db_obra, estante.estado,
                                 data_inicio, data_fim)

        try:
            self.session.add(db_estante)
            self.session.commit()
            self.session.refresh(db_estante)
        except IntegrityError:
            raise BadRequestException(detail="Obra já existe na estante.")

        return estante

    def remove_item(self, idUsuario: int, idObra: int) -> schemaEstante:
        item = self.get_obra_user(idUsuario, idObra)
        res = schemaEstante.from_orm(item)

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
        self.session.refresh(obra)

        return obra
