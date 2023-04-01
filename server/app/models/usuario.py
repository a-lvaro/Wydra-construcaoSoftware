from sqlalchemy import Column, Table, String, Integer
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


# Entidade Avaliação
class Avaliacao(Base):
    __tablename__ = "AVALIACAO"

    id: Mapped[int] = mapped_column("ID_AVALIACAO", primary_key=True)
    nota = Column("NOTA", Integer, nullable=True)
    resenha = Column("RESENHA", String(1000), nullable=True)
    data = Column("DATA", DateTime, nullable=False)

    id_usuario: Mapped[int] = mapped_column(ForeignKey("USUARIO.ID_USUARIO"))
    usuario: Mapped["Usuario"] = relationship(back_populates="avaliacoes")
    id_obra = Column("ID_OBRA", Integer, nullable=False)

    def __init__(self, usuario, id_obra, nota, resenha):
        self.id_obra = id_obra
        self.nota = nota
        self.resenha = resenha
        self.data = datetime.now()
