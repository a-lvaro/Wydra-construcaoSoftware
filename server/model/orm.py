from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import Table
from datetime import datetime


DATABASE_URL = 'sqlite:///model/Wydra.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# DEFINIÇÃO DO SCHEMA DO BANCO DE DADOS

from core.database import get_session

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


# Entidade Avaliação
class Avaliacao(Base):
    __tablename__ = "AVALIACAO"

    id_comentario = Column("ID_COMENTARIO", Integer, primary_key=True)
    id_usuario = Column("ID_USUARIO", Integer, ForeignKey(
        'USUARIO.ID_USUARIO'), nullable=False)
    id_obra = Column("ID_OBRA", Integer, nullable=False)
    nota = Column("NOTA", Integer, nullable=True)
    texto = Column("TEXTO", String(300), nullable=False)
    data_comentario = Column("DATA_COMENTARIO", DateTime, nullable=False)

    def __init__(self, id_usuario, id_obra, nota, texto):
        self.id_usuario = id_usuario
        self.id_obra = id_obra
        self.nota = nota
        self.texto = texto
        self.data_comentario = datetime.now()
