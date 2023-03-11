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


class ObrasEstante(Base):
    __tablename__ = "ESTANTE"

    id_usuario = Column("ID_USUARIO", Integer, ForeignKey(
        'USUARIO.ID_USUARIO'), primary_key=True)
    id_obra = Column("ID_OBRA", Integer, primary_key=True)
    estado = Column(Enum('Lista de Desejos', 'Em progresso',
                    'Finalizada', 'Abandonada', name='ESTADO'), nullable=False)
    nota = Column("NOTA", Integer, nullable=True)
    data_inicio = Column("DATA_INICIO", DateTime, nullable=True)
    data_fim = Column("DATA_FIM", DateTime, nullable=True)

    def __init__(self, id_usuario, id_obra, estado, nota, data_inicio, data_fim):
        # self.id_usuario = id_usuario
        self.id_obra = id_obra
        self.estado = estado
        self.nota = nota
        self.data_inicio = data_inicio
        self.data_fim = data_fim

    def __repr__(self):
        return f"ObrasEstante(id_usuario={self.id_usuario!r}, id_obra={self.id_obra!r}, estado={self.estado!r}, nota={self.nota!r}, data_inicio={self.data_inicio!r}, data_fim={self.data_fim!r})"


engine = create_engine('sqlite:///server/model/database.db', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

usuario = Usuario("João", "ola@gmail.com", "123456")
session.add(usuario)
session.commit()
