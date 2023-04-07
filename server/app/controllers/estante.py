from datetime import datetime
from typing import List

from sqlalchemy.orm.exc import NoResultFound
from fastapi import HTTPException

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
    
    def getObraUsuario(self, idUsuario: int, idObra: int) -> schemaEstante:
        try:
            obraEstanteUsuario = self.session.query(ItemEstante).filter(
                ItemEstante.id_usuario == idUsuario,
                ItemEstante.id_obra == idObra).one()

            return obraEstanteUsuario
        except NoResultFound:
            raise HTTPException(status_code=404, detail="Item not found")


    def add(self, user :int, estante: schemaEstante) -> schemaEstante:
        if estante.estado in [EstadoObra.finalizada, EstadoObra.abandonada]:
            data_inicio = datetime.now()
            data_fim = datetime.now()
        else:
            data_inicio = datetime.now()
            data_fim = None

        db_obra = self.obra_ctrl.get(estante.obra.id)
        db_estante = ItemEstante(user, db_obra, estante.estado, 
                                 data_inicio, data_fim)

        self.session.add(db_estante)
        self.session.commit()
        self.session.refresh(db_estante)

        return estante

    def remove_item(self, idUsuario :int, idObra :int) -> schemaEstante:
        item = self.session.query(ItemEstante).filter(
            ItemEstante.id_usuario == idUsuario,
            ItemEstante.id_obra == idObra).first()

        estante = schemaEstante.from_orm(item)

        self.session.delete(item)
        self.session.commit()

        return estante

    def update_item(self, idUsuario :int, idObra :int, novoEstado :int):
        obra = self.session.query(ItemEstante).filter(
            ItemEstante.id_usuario == idUsuario, ItemEstante.id_obra == idObra
        ).first()

        obra.estado = novoEstado

        if novoEstado in [EstadoObra.finalizada, EstadoObra.abandonada]:
            obra.data_fim = datetime.now()
        elif novoEstado == EstadoObra.em_progresso:
            obra.data_inicio = datetime.now()

        self.session.commit()
        self.session.refresh(obra)

        return obra
