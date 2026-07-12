from collections.abc import Callable

from backend.config.settings import Settings

MessageHandler = Callable[[bytes], None]


class RabbitMQConsumer:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def consume(self, queue_name: str, handler: MessageHandler | None = None) -> None:
        # Adapter placeholder. Wire pika here when real transcoding jobs are introduced.
        _ = (self._settings.rabbitmq_url, queue_name, handler)
