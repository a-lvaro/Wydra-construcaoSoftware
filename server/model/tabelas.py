from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy import ForeignKey, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from bcrypt import hashpw, gensalt, checkpw
from datetime import datetime


Base = declarative_base()


class Usuario(Base):
    __tablename__ = "USUARIO"

    id_usuario = Column("ID_USUARIO", Integer, primary_key=True)
    nome = Column("NOME", String(30), nullable=False)
    email = Column("EMAIL", String(30), nullable=False)
    senha = Column("SENHA", String(64), nullable=False)
    caminho_foto = Column("CAMINHO_FOTO", String(100), nullable=True)
    data_cadastro = Column("DATA_CADASTRO", DateTime, nullable=False)

    def __repr__(self) -> str:
        return f"usuário(id={self.id!r}, nome={self.nome!r}, email={self.email!r})"

    def __init__(self, nome, email, senha, caminho_foto=None):
        self.nome = nome
        self.email = email
        self.senha = hashpw(senha.encode('utf-8'), gensalt()).decode('utf-8')
        self.caminho_foto = caminho_foto
        self.data_cadastro = datetime.now()

    @staticmethod
    def authenticate(session, email, senha):
        user = session.query(Usuario).filter_by(email=email).first()
        if user and checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
            return user
        else:
            return None


class Seguidores(Base):
    __tablename__ = "SEGUIDORES"

    id_usuario = Column("ID_USUARIO", Integer, ForeignKey(
        'USUARIO.ID_USUARIO'), primary_key=True)
    id_seguidor = Column("ID_SEGUIDOR", Integer, ForeignKey(
        'USUARIO.ID_USUARIO'), primary_key=True)

    def __init__(self, id_usuario, id_seguidor):
        self.id_usuario = id_usuario
        self.id_seguidor = id_seguidor

    def __repr__(self):
        return f"Seguidores(id_usuario={self.id_usuario!r}, id_seguidor={self.id_seguidor!r})"


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


engine = create_engine('sqlite:///server/model/Wydra.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

usuario = Usuario("João", "ola@gmail.com", "123456")
session.add(usuario)
session.commit()
