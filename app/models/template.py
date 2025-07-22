from sqlalchemy import Column, String, Enum, DateTime
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from app.db.session import Base
from app.models.enums import NotificationChannel

class Template(Base):
    __tablename__ = "templates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    language = Column(String, nullable=False)  # e.g. "en", "ka"
    channel = Column(Enum(NotificationChannel), nullable=False)
    title_tpl = Column(String, nullable=True)
    body_tpl = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Template(name={self.name}, channel={self.channel})>"
