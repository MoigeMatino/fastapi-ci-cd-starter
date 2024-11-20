import os

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    postgres_db: str
    postgres_user: str
    postgres_password: str
    db_host: str
    db_port: str
    
    class Config:
        env_file = ".env"
    
def get_settings():
    return Settings()