from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str
    redis_url: str
    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/0"
    redis_host: str
    redis_port: int
    database_url: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()