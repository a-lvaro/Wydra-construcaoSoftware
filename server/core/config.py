from enum import Enum

from pydantic import BaseSettings

class Tags(Enum):
    user = "Usuário"
    estante = "Estante"
    avaliacao = "Avaliações"
    obra = "Obras"
    
class EnvironmentType(str, Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"

class BaseConfig(BaseSettings):
    class Config:
        case_sensitive = True

class Config(BaseConfig):
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    DATABASE_URL: str = 'sqlite:///core/database/Wydra.db'
    RELEASE_VERSION: str = "0.1"
    SHOW_SQL_ALCHEMY_QUERIES: int = 0
    SECRET_KEY: str = "super-secret-key"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRE_MINUTES: int = 60

config: Config = Config()

