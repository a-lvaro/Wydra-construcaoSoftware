from sqlalchemy.exc import IntegrityError
from typing import List

from core.exceptions import NotFoundException, BadRequestException
from app.schemas import Avaliacao, AvaliacaoCreate, Usuario, ObraNota
from app.models import Avaliacao as ormAvaliacao

from .usuario import ControladorUsuario
from .obra import ControladorObra


class ControladorAvaliacao:
    def __init__(self, session):
        self.session = session
        self.user_ctrl = ControladorUsuario(session)
        self.obra_ctrl = ControladorObra(session)

    def create(self, usuario: Usuario, avaliacao: AvaliacaoCreate) -> Avaliacao:
        db_obra = self.obra_ctrl.get(avaliacao.obra.id)

        if db_obra:
            # atualiza a nota da obra se ela existe
            total = 0
            for a in db_obra.avaliacoes:
                total += a.nota
            db_obra.nota = (total + avaliacao.nota) / (len(db_obra.avaliacoes) + 1)
        else:
            # cria uma nova obra com a nota da avaliação
            obra = ObraNota(id=avaliacao.obra.id, nota=avaliacao.nota)
            db_obra = self.obra_ctrl.create(obra)

        db_avaliacao = ormAvaliacao(
            usuario, avaliacao.nota, db_obra, avaliacao.resenha, 0)

        try:
            self.session.add(db_avaliacao)
            self.session.commit()

        except IntegrityError:
            raise BadRequestException(detail="Avaliação já existe")

        return db_avaliacao

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

        return db_avaliacao

    def get_by_user(self, id: int):
        user = self.user_ctrl.get(id)
        return user.avaliacoes

    def get_by_obra(self, id: int):
        obra = self.obra_ctrl.get(id)
        return obra.avaliacoes

