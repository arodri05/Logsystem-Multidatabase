from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # App Settings
    APP_NAME: str = "Sistema de Logs Multi Base de Datos"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    SQLITE_PATH: str = "metadata.db"
    WEB_CONCURRENCY: int = 1

    # MariaDB
    MARIADB_HOST: str = Field(default="mariadb")
    MARIADB_PORT: int = Field(default=3306)
    MARIADB_DATABASE: str = Field(default="logs")
    MARIADB_USER: str = Field(default="root")
    MARIADB_PASSWORD: str = Field(default="root")

    # PostgreSQL
    POSTGRES_HOST: str = "postgres"
    POSTGRES_PORT: int = 5432
    POSTGRES_DATABASE: str = "logs"
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"

    # SQL Server
    SQLSERVER_HOST: str = "sqlserver"
    SQLSERVER_PORT: int = 1433
    SQLSERVER_DATABASE: str = "logs"
    SQLSERVER_USER: str = "sa"
    SQLSERVER_PASSWORD: str = "YourStrongPassword123"

    # MongoDB
    MONGO_HOST: str = "mongo"
    MONGO_PORT: int = 27017
    MONGO_DATABASE: str = "logs"

    # Redis
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379

    model_config = {
        "env_file": ".env",
        "case_sensitive": False
    }

settings = Settings()
