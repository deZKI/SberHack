import os

from pydantic_settings import BaseSettings, SettingsConfigDict

DOTENV = os.path.join(os.path.dirname(__file__), ".env")


class Settings(BaseSettings):
    """ Настройки проекта """
    DB_HOST: str
    DB_PORT: int

    GIGA_CHAT_KEY: str

    model_config = SettingsConfigDict(env_file=DOTENV)


settings = Settings()
