from app.services.channels.BaseNotification import BaseChannel


class EmailChannel(BaseChannel):
    """
    Email channel for sending notifications.
    """

    def send(self, recipient: dict, subject: str, body: str, **kwargs) -> None:
        """
        Send an email notification to the recipient.
        """
        pass