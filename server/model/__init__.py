import tmdbsimple as tmdb

from . import orm

# Cria tabelas no banco de dados sqlite
orm.Base.metadata.create_all(orm.engine)

# Inicializa API tmdb
API_KEY = '158133b16a544083e8506dccf5af2bd4'
tmdb.API_KEY = API_KEY
