from sqlalchemy import Column, Integer, String, Boolean, Enum, DateTime, ForeignKey, JSON
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime


from app.db.session import Base
from app.models.enums import NotificationType, NotificationChannel, NotificationStatus

class Notification(Base):
    __tablename__ = "notifications"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    template_code = Column(String, nullable=False)
    channel = Column(Enum(NotificationChannel), nullable=False)
    recipient_id = Column(String, nullable=False)
    recipient = Column(JSONB, nullable=False)
    data = Column(JSONB, nullable=False)
    language = Column(String, default="ka")
    title = Column(String, nullable=True)
    message = Column(String, nullable=True)
    status = Column(Enum(NotificationStatus), nullable=False, server_default=NotificationStatus.pending)
    type = Column(Enum(NotificationType), nullable=False, default=NotificationType.info)
    template_id = Column(UUID(as_uuid=True), ForeignKey("templates.id"), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    sent_at = Column(DateTime, nullable=True)

    delivery_logs = relationship("DeliveryLog", back_populates="notification", cascade="all, delete-orphan")


