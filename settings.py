from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URI: str = 'sqlite+aiosqlite:///:memory:"'

    model_config = SettingsConfigDict(env_file='.env')

settings = Settings()
