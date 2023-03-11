# https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91

import sqlalchemy as db
from bcrypt import hashpw, gensalt, checkpw
from datetime import datetime

# Crie uma conexão com o banco de dados PostgreSQL

from tabelas import Usuario


engine = db.create_engine('sqlite:///server/model/Wydra.db')
connection = engine.connect()
metadata = db.MetaData()

# Inserting record one by one
query = db.insert(Usuario).values(
    'romulo', 'mincache', '123456', active=True)
ResultProxy = connection.execute(query)

# usuario = db.Table('USUARIO', metadata, autoload=True, autoload_with=engine)

# query = db.select([usuario])
# ResultProxy = connection.execute(query)
# ResultSet = ResultProxy.fetchall()

# print(ResultSet)
