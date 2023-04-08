from typing import List

from app.schemas import Avaliacao, AvaliacaoBase, Usuario
from app.models import Avaliacao as ormAvaliacao

from .usuario import ControladorUsuario
from .obra import ControladorObra

class ControladorAvaliacao:
    def __init__(self, session):
        self.session = session
        self.user_ctrl = ControladorUsuario(session)
        self.obra_ctrl = ControladorObra(session)

    def get(self, id: int) -> Avaliacao:
        avaliacao = self.session.query(ormAvaliacao).filter(
            ormAvaliacao.id == id).first()

        return avaliacao

    def create(self, usuario: Usuario, avaliacao: AvaliacaoBase) -> Avaliacao:
        db_obra = self.obra_ctrl.get(avaliacao.obra.id)

        db_avaliacao = ormAvaliacao(usuario, avaliacao.nota, db_obra, avaliacao.resenha)

        self.session.add(db_avaliacao)
        self.session.commit()
        self.session.refresh(db_avaliacao)

        return avaliacao
    
    def get_by_user(self, id: int) -> List[AvaliacaoBase]:
        user = self.user_ctrl.get(id)
        return user.avaliacoes

    def get_by_obra(self, id: int) -> List[Avaliacao]:
        obra = self.obra_ctrl.get(id)
        return obra.avaliacoes