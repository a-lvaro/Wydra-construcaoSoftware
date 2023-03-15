from . import orm

# Cria tabelas no banco de dados sqlite
orm.Base.metadata.create_all(orm.engine)
