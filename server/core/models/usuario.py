from core.database import get_session

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

    nick = Column("NICK", String(16), unique=True, nullable=False)
    email = Column("EMAIL", String(64), unique=True, nullable=False)

    nome = Column("NOME", String(64), nullable=False)
    sobrenome = Column("SOBRENOME", String(64), nullable=False)

    senha = Column("SENHA", String(64), nullable=False)

    data_cadastro = Column("DATA_CADASTRO", DateTime, nullable=False)
    caminho_foto = Column("CAMINHO_FOTO", String(100), nullable=True)

    # Relacionamento entre Seguidores
    seguidores = relationship(
        "Usuario",
        secondary=relacao_seguidores,
        primaryjoin=id == relacao_seguidores.c.ID_USUARIO,
        secondaryjoin=id == relacao_seguidores.c.ID_SEGUIDOR,
        backref="seguindo"
    )

