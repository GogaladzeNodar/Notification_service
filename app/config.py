from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    app_name: str

    #redis/celery
    redis_url: str
    celery_broker_url: str = "redis://localhost:6379/0"
    celery_result_backend: str = "redis://localhost:6379/0"
    redis_host: str
    redis_port: int

    #database
    async_database_url: str
    sync_database_url: str



    #email settings
    smtp_server: str
    smtp_port: int
    smtp_username: str
    smtp_password: str
    use_tls: bool = True
    use_ssl: bool = False
    from_email: str
    from_name: str = "Notification Service"

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()