from sqlalchemy import Column, Enum, String, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid

from app.database import Base
from app.models.enums import NotificationChannel, NotificationStatus


class DeliveryLog(Base):
    __tablename__ = "delivery_logs"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    notification_id = Column(UUID(as_uuid=True), ForeignKey("notifications.id"), nullable=False)
    channel = Column(Enum(NotificationChannel), nullable=False)
    status = Column(Enum(NotificationStatus), nullable=False, default=NotificationStatus.pending)
    error_message = Column(String, nullable=True)
    sent_at = Column(DateTime, nullable=True, default=None)

    notification = relationship("Notification", back_populates="delivery_logs")