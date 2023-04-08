from app.schemas import Obra, TipoObra
from app.models import Obra as ormObra


class ControladorObra:
    def __init__(self, session):
        self.session = session

    def get(self, id: int, tipo: TipoObra = TipoObra.filme) -> Obra:
        obra = self.session.query(ormObra).filter(
            ormObra.id == id).first()

        # cria obra no banco de dados quando ela não existe ainda
        if not obra:
            obra = self.create(Obra(id=id, tipo=tipo))

        return obra

    def create(self, obra: Obra):
        db_obra = ormObra(obra.id, obra.tipo)

        self.session.add(db_obra)
        self.session.commit()
        self.session.refresh(db_obra)

        return db_obra
