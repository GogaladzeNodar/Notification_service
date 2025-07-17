from app.services.channels.BaseNotification import BaseChannel

class SMSChannel(BaseChannel):
    """
    SMS channel for sending notifications.
    """

    def send(self, recipient: dict, message: str, **kwargs) -> None:
        """
        Send an SMS notification to the recipient.
        """
        pass