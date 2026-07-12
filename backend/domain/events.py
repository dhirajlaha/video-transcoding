from dataclasses import dataclass
from datetime import UTC, datetime
from uuid import UUID


@dataclass(frozen=True, slots=True)
class DomainEvent:
    occurred_at: datetime


@dataclass(frozen=True, slots=True)
class VideoUploadCreated(DomainEvent):
    video_id: UUID
    object_key: str


def now_utc() -> datetime:
    return datetime.now(tz=UTC)
