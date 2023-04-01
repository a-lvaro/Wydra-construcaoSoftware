from core.database import Base, engine

from .estante import Estante
from .usuario import Usuario

# Cria tabelas no banco de dados sqlite
Base.metadata.create_all(engine)
