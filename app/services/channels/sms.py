from app.services.channels.base_notification import BaseChannels


class SMSChannel(BaseChannels):
    """
    SMS channel for sending notifications.
    """

    def send_notification(self, recipient: dict, message: str, **kwargs) -> None:
        """
        Send an SMS notification to the recipient.
        """
        print(f"[MOCK SMS] Sending SMS to {recipient['phone']}: {message}")