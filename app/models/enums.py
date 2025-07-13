from enum import Enum

class NotificationType(str, Enum):
    info = "info"
    warning = "warning"
    error = "error"
    success = "success"
    

class NotificationStatus(str, Enum):
    pending = "pending"
    sent = "sent"
    failed = "failed"


class NotificationChannel(str, Enum):
    email = "email"
    sms = "sms"
    push = "push"
    websocket = "websocket"