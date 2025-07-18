from app.services.channels.channel_factory import get_channel


class NotificationDispatcher:
    def __init__(self, channel_factory=get_channel):
        self.channel_factory = channel_factory

    def dispatch(self, channel: str, recipient: dict, message: str) -> None:
        strategy = self.channel_factory(channel)
        strategy.send_notification(recipient, message)