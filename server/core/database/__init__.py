from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import core.config
DATABASE_URL = core.config.DATABASE_URL

engine = create_engine(DATABASE_URL,
                       connect_args={"check_same_thread": False},
                       pool_size=20, max_overflow=30)

Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_session():
    db = Session()
    return db
