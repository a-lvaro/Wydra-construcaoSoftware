from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from bcrypt import hashpw, gensalt, checkpw


Base = declarative_base()


class Usuario(Base):
    __tablename__ = "USUARIO"

    id_usuario = Column("ID_USUARIO", Integer, primary_key=True)
    nome = Column("NOME", String(30), nullable=False)
    email = Column("EMAIL", String(30), nullable=False)
    senha = Column("SENHA", String(64), nullable=False)
    caminho_foto = Column("CAMINHO_FOTO", String(100), nullable=True)

    def __repr__(self) -> str:
        return f"usuário(id={self.id!r}, nome={self.nome!r}, email={self.email!r})"

    @staticmethod
    def authenticate(session, email, senha):
        user = session.query(Usuario).filter_by(email=email).first()
        if user and checkpw(senha.encode('utf-8'), user.senha.encode('utf-8')):
            return user
        else:
            return None


class ObrasEstante(Base):
    __tablename__ = "ESTANTE"

    id_obra_estante = Column("ID_OBRA_ESTANTE", Integer, primary_key=True)
    id_usuario = Column("ID_USUARIO", Integer, ForeignKey(
        'usuario.id_usuario'), primary_key=True)
    id_obra = Column("ID_OBRA", Integer, nullable=False)
    estado = Column(Enum('Lista de Desejos', 'Em progresso',
                    'Finalizada', 'Abandonada', name='ESTADO'), nullable=False)
    nota = Column("NOTA", Integer, nullable=True)
    data_inicio = Column("DATA_INICIO", DateTime, nullable=True)
    data_fim = Column("DATA_FIM", DateTime, nullable=True)

    user_id = Column(Integer, ForeignKey('usuario.id_usuario'))
    usuario = relationship("Usuario", backref="obras_estante")
