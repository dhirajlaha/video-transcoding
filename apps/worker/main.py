from backend.config.settings import Settings
from backend.infrastructure.queue import RabbitMQConsumer


def main() -> None:
    settings = Settings()
    consumer = RabbitMQConsumer(settings=settings)
    consumer.consume(queue_name="video-transcoding")


if __name__ == "__main__":
    main()
