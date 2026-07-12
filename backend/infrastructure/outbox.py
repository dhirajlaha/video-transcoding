import json
from dataclasses import asdict

from sqlalchemy.orm import Session

from backend.domain.events import DomainEvent
from backend.infrastructure.models import OutboxMessage


class SqlAlchemyOutbox:
    def __init__(self, session: Session) -> None:
        self._session = session

    def add(self, event: DomainEvent) -> None:
        self._session.add(
            OutboxMessage(
                event_type=event.__class__.__name__,
                payload=json.dumps(asdict(event), default=str),
            )
        )
