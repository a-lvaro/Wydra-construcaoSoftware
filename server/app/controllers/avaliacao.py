from typing import List

from core.exceptions import NotFoundException
from app.schemas import Avaliacao, AvaliacaoBase, Usuario
from app.models import Avaliacao as ormAvaliacao

from .usuario import ControladorUsuario
from .obra import ControladorObra


class ControladorAvaliacao:
    def __init__(self, session):
        self.session = session
        self.user_ctrl = ControladorUsuario(session)
        self.obra_ctrl = ControladorObra(session)

    def create(self, usuario: Usuario, avaliacao: AvaliacaoBase) -> Avaliacao:
        db_obra = self.obra_ctrl.get(avaliacao.obra.id)

        db_avaliacao = ormAvaliacao(
            usuario, avaliacao.nota, db_obra, avaliacao.resenha, 0)

        self.session.add(db_avaliacao)
        self.session.commit()
        self.session.refresh(db_avaliacao)

        return avaliacao

    def curtir(self, idUsuario: int, idObra: int,
               curtida: bool) -> Avaliacao:

        db_avaliacao = self.session.query(ormAvaliacao).filter(
            ormAvaliacao.id_usuario == idUsuario,
            ormAvaliacao.id_obra == idObra).first()

        if not db_avaliacao:
            raise NotFoundException(detail="Avaliação não existe.")

        if curtida:
            db_avaliacao.curtidas += 1
        else:
            db_avaliacao.curtidas -= 1

        self.session.commit()
        self.session.refresh(db_avaliacao)

        return db_avaliacao

    def get_by_user(self, id: int) -> List[AvaliacaoBase]:
        user = self.user_ctrl.get(id)
        return user.avaliacoes

    def get_by_obra(self, id: int) -> List[Avaliacao]:
        obra = self.obra_ctrl.get(id)
        return obra.avaliacoes
