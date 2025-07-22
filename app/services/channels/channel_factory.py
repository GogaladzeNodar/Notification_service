from app.services.channels.base_notification import BaseChannels
from app.services.channels.email import EmailChannel
from app.services.channels.sms import SMSChannel


def get_channel(channel_type: str) -> BaseChannels:
    """
    Factory function to get the appropriate channel instance based on the channel type.
    
    Args:
        channel_type (str): The type of channel ("sms", "email", etc.).
    
    Returns:
        BaseChannel: An instance of the appropriate channel class.
    
    Raises:
        ValueError: If the channel type is not supported.
    """
    if channel_type == "sms":
        return SMSChannel()
    elif channel_type == "email":
        return EmailChannel()
    else:
        raise ValueError(f"Unsupported channel type: {channel_type}")