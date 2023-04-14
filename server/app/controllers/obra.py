from app.schemas import Obra, ObraNota, TipoObra
from app.models import Obra as ormObra


class ControladorObra:
    def __init__(self, session):
        self.session = session

    def get(self, id: int):
        obra = self.session.query(ormObra).filter(
            ormObra.id == id).first()

        return obra

    def get_or_create(self, id: int, tipo: TipoObra = TipoObra.filme):
        obra = self.get(id)

        # cria obra no banco de dados quando ela não existe ainda
        if not obra:
            obra = self.create(Obra(id=id, tipo=tipo))

        return obra

    def create(self, obra: ObraNota):
        db_obra = ormObra(id=obra.id, nota=obra.nota,  tipo=obra.tipo)

        self.session.add(db_obra)

        return db_obra
