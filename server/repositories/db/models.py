from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from . import Base

class User(Base):
    __tablename__ = "USUARIO"

    id = Column("ID_USUARIO", Integer, primary_key=True)
    name = Column("NOME", String(30), nullable=False)
    email = Column("EMAIL", String(30), nullable=False)
    password = Column("SENHA", String(64), nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"


