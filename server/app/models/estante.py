from sqlalchemy import Column
from sqlalchemy import ForeignKey, String, Integer, DateTime

from core.database import Base

# Entidade Estante
class Estante(Base):
    __tablename__ = "ESTANTE"

    id_usuario = Column("ID_USUARIO", Integer, ForeignKey(
        'USUARIO.ID_USUARIO'), primary_key=True)
    id_obra = Column("ID_OBRA", Integer, primary_key=True)
    estado = Column(Enum('Lista de Desejos', 'Em progresso',
                    'Finalizada', 'Abandonada', name='ESTADO'), nullable=False)
    tipo = Column(Enum('Manga', 'Anime', 'Livro', 'Filme',
                  'Série', name='TIPO'), nullable=False)

    data_inicio = Column("DATA_INICIO", DateTime, nullable=True)
    data_fim = Column("DATA_FIM", DateTime, nullable=True)

    def __init__(self, id_usuario, id_obra, estado, data_inicio, data_fim):
        self.id_usuario = id_usuario
        self.id_obra = id_obra
        self.estado = estado
        self.data_inicio = data_inicio
        self.data_fim = data_fim


