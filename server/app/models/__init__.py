from core.database import Base, engine

from .models import Usuario, ItemEstante, Avaliacao, Obra

# Cria tabelas no banco de dados sqlite
Base.metadata.create_all(engine)
