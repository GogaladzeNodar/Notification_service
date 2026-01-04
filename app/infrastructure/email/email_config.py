from fastapi_mail import ConnectionConfig, FastMail
from app.config import settings

def build_fast_mail() -> FastMail:
    conf = ConnectionConfig(
        MAIL_USERNAME=settings.smtp_username,
        MAIL_PASSWORD=settings.smtp_password,
        MAIL_FROM=settings.from_email,
        MAIL_FROM_NAME=settings.from_name,
        MAIL_SERVER=settings.smtp_server,
        MAIL_PORT=settings.smtp_port,
        MAIL_STARTTLS=settings.use_tls,
        MAIL_SSL_TLS=settings.use_ssl,
        USE_CREDENTIALS=True,
        VALIDATE_CERTS=True,
    )
    return FastMail(conf)