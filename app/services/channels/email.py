from app.services.channels.base_notification import BaseChannels



class EmailChannel(BaseChannels):
    """
    Email channel for sending notifications.
    """

    def send_notification(self, recipient: dict, message: str, **kwargs) -> None:
        """
        Send an email notification to the recipient.
        """
        print(f"[MOCK email] Sending SMS to {recipient['email']}: {message}")