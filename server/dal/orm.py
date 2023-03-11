from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://wydra:wydra@localhost/WYDRA"
engine = create_engine(DATABASE_URL)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

class User(Base):
    __tablename__ = "USUARIO"

    id = Column("ID_USUARIO", Integer, primary_key=True)
    name = Column("NOME", String(30), nullable=False)
    email = Column("EMAIL", String(30), nullable=False)
    password = Column("SENHA", String(64), nullable=False)

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, email={self.email!r})"

