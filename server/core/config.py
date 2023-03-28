from enum import Enum

from pydantic import BaseSettings, PostgresDsn, RedisDsn

class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True


class Config(BaseConfig):
    DATABASE_URL: str = 'sqlite:///core/database/Wydra.db'
    RELEASE_VERSION: str = "0.1"
    SHOW_SQL_ALCHEMY_QUERIES: int = 0
    SECRET_KEY: str = "super-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60 * 24

config: Config = Config()
