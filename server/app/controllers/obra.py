from app.schemas import Obra, ObraNota, TipoObra
from app.models import Obra as ormObra


class ControladorObra:
    def __init__(self, session):
        self.session = session

    def get(self, id: int) -> ormObra:
        obra = self.session.query(ormObra).filter(
            ormObra.id == id).first()

        return obra

    def create(self, obra: ObraNota) -> ormObra:
        db_obra = ormObra(id=obra.id, nota=obra.nota,  tipo=obra.tipo)

        self.session.add(db_obra)

        return db_obra
