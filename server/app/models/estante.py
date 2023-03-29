from sqlalchemy import Column, ForeignKey
from sqlalchemy import String, Integer, DateTime, Enum

from core.database import Base

# Entidade Estante
class Estante(Base):
    __tablename__ = "ESTANTE"

    id_usuario = Column("ID_USUARIO", Integer, ForeignKey(
        'USUARIO.ID_USUARIO'), primary_key=True)
    id_obra = Column("ID_OBRA", Integer, primary_key=True)
    estado = Column(Enum('Lista de Desejos', 'Em progresso',
                    'Finalizada', 'Abandonada', name='ESTADO'), nullable=False)
    tipo = Column(Enum('Livro', 'Filme',
                  'Série', name='TIPO'), nullable=False)
                  
    data_inicio = Column("DATA_INICIO", DateTime, nullable=True)
    data_fim = Column("DATA_FIM", DateTime, nullable=True)



