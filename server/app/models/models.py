from sqlalchemy import Column, Table, String, Integer, Float
from sqlalchemy import DateTime, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from typing import Optional, List
from datetime import datetime

from core.database import Base

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
    id: Mapped[int] = mapped_column("ID_USUARIO", primary_key=True)

    nick = Column("NICK", String(16), unique=True, nullable=False)
    email = Column("EMAIL", String(64), unique=True, nullable=False)

    nome = Column("NOME", String(64), nullable=False)
    sobrenome = Column("SOBRENOME", String(64), nullable=False)

    senha = Column("SENHA", String(64), nullable=False)

    data_cadastro = Column("DATA_CADASTRO", DateTime, nullable=False)
    caminho_foto = Column("CAMINHO_FOTO", String(100), nullable=True)

    avaliacoes: Mapped[Optional[List["Avaliacao"]]] = relationship(
        back_populates="usuario")

    estante: Mapped[List["ItemEstante"]] = relationship(
        back_populates="usuario")

    # Relacionamento entre Seguidores
    seguidores = relationship(
        "Usuario",
        secondary=relacao_seguidores,
        primaryjoin=id == relacao_seguidores.c.ID_USUARIO,
        secondaryjoin=id == relacao_seguidores.c.ID_SEGUIDOR,
        backref="seguindo"
    )

    def __init__(self, nick, nome, sobrenome, email, senha, caminho_foto=None):
        self.nick = nick
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha
        self.caminho_foto = caminho_foto

        self.data_cadastro = datetime.now()


# Entidade Avaliação
class Avaliacao(Base):
    __tablename__ = "AVALIACAO"

    nota = Column("NOTA", Integer, nullable=True)
    resenha = Column("RESENHA", String(1000), nullable=True)
    data = Column("DATA", DateTime, nullable=False)
    curtidas = Column("CURTIDA", Integer, nullable=True, default=0)

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("USUARIO.ID_USUARIO"), primary_key=True)
    usuario: Mapped["Usuario"] = relationship(back_populates="avaliacoes")

    id_obra: Mapped[int] = mapped_column(
        ForeignKey("OBRA.ID_OBRA"), primary_key=True)
    obra: Mapped["Obra"] = relationship(back_populates="avaliacoes")

    def __init__(self, usuario, nota, obra, resenha, curtida):
        self.usuario = usuario
        self.id_usuario = usuario.id

        self.obra = obra
        self.id_obra = obra.id
        self.nota = nota
        self.resenha = resenha
        self.curtida = curtida
        self.data = datetime.now()

        


class ItemEstante(Base):
    __tablename__ = "ESTANTE"

    id_usuario: Mapped[int] = mapped_column(
        ForeignKey("USUARIO.ID_USUARIO"), primary_key=True)

    usuario: Mapped["Usuario"] = relationship(back_populates="estante")

    id_obra: Mapped[int] = mapped_column(
        ForeignKey("OBRA.ID_OBRA"), primary_key=True)
    obra: Mapped["Obra"] = relationship()

    estado = Column('ESTADO', Integer, nullable=False)

    data_inicio = Column("DATA_INICIO", DateTime, nullable=True)
    data_fim = Column("DATA_FIM", DateTime, nullable=True)

    def __init__(self, user, obra, estado,
                 data_inicio, data_fim):

        self.usuario = user
        self.id_usuario = user.id
        self.obra = obra
        self.id_obra = obra.id
        self.estado = estado
        self.data_inicio = data_inicio
        self.data_fim = data_fim


class Obra(Base):
    __tablename__ = "OBRA"

    id = Column("ID_OBRA", Integer, nullable=False,
                primary_key=True, autoincrement=False)
    tipo = Column('TIPO_OBRA', Integer, nullable=False)
    nota = Column('MEDIA_NOTA', Float, nullable=False)

    avaliacoes: Mapped[Optional[List["Avaliacao"]]] = relationship(
        back_populates="obra")

    def __init__(self, id, tipo, nota=0):
        self.id = id
        self.tipo = tipo
        self.nota = nota

    def __eq__(self, other):
        return self.id == self.id and \
               self.tipo == self.tipo and \
               self.nota == self.nota 
