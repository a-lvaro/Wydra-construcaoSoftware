from core.database import Base, engine

from .avaliacao import *
from .estante import *
from .usuario import *

# Cria tabelas no banco de dados sqlite
Base.metadata.create_all(engine)