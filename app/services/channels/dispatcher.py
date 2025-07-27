from app.services.channels.channel_factory import ChannelFactory
from app.services.channels.base_notification import BaseChannels


class NotificationDispatcher:
    def __init__(self, channel_factory: ChannelFactory = ChannelFactory()):
        self.channel_factory = channel_factory

    async def dispatch(self, channel_type: str, recipient: dict,  message: str) -> None:
        strategy: BaseChannels = self.channel_factory.get_channel(channel_type)
        await strategy.send_notification(recipient, message)