from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import ForeignKey, DateTime, create_engine
from sqlalchemy.orm import relationship
from sqlalchemy import Table


DATABASE_URL = 'sqlite:///../db/Wydra.db'
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# DEFINIÇÃO DO SCHEMA DO BANCO DE DADOS

# Relacionamento entre Seguidores
relacao_seguidores = Table(
    "SEGUIDORES",
    Base.metadata,
    Column("ID_USUARIO", ForeignKey("USUARIO.ID_USUARIO"), primary_key=True),
    Column("ID_SEGUIDOR", ForeignKey("USUARIO.ID_USUARIO"), primary_key=True)
)

# Entidade Usuário
class Usuario(Base):
    __tablename__ = "USUARIO"

    # Atributos do Usuário
    id = Column("ID_USUARIO", Integer, primary_key=True)
    
    nome = Column("NOME", String(30), nullable=False)
    email = Column("EMAIL", String(30), nullable=False)
    senha = Column("SENHA", String(64), nullable=False)

    data_cadastro = Column("DATA_CADASTRO", DateTime, nullable=False)
    caminho_foto = Column("CAMINHO_FOTO", String(100), nullable=True)
    
    # Relacionamento entre Seguidores
    seguidores = relationship(
        "Usuario",
        secondary = relacao_seguidores,
        primaryjoin = id == relacao_seguidores.c.ID_USUARIO,
        secondaryjoin = id == relacao_seguidores.c.ID_SEGUIDOR,
        backref = "seguindo"
    )

    def __repr__(self) -> str:
        return f"usuário(id={self.id!r}, nome={self.nome!r}, email={self.email!r})"


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

    def __repr__(self):
        return f"Estante(id_usuario={self.id_usuario!r}, id_obra={self.id_obra!r}, estado={self.estado!r}, nota={self.nota!r}, data_inicio={self.data_inicio!r}, data_fim={self.data_fim!r})"

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

    def __repr__(self):
        return f"Comentario(id_usuario={self.id_usuario!r}, id_obra={self.id_obra!r}, texto={self.texto!r}, data_comentario={self.data_comentario!r})"

