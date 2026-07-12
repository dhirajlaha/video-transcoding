from dataclasses import dataclass, field
from uuid import UUID, uuid4

from backend.domain.events import DomainEvent, VideoUploadCreated, now_utc


@dataclass(slots=True)
class Video:
    filename: str
    content_type: str
    id: UUID = field(default_factory=uuid4)
    _events: list[DomainEvent] = field(default_factory=list)

    @classmethod
    def create_upload(cls, filename: str, content_type: str) -> "Video":
        video = cls(filename=filename, content_type=content_type)
        video._events.append(
            VideoUploadCreated(
                occurred_at=now_utc(),
                video_id=video.id,
                object_key=video.object_key,
            )
        )
        return video

    @property
    def object_key(self) -> str:
        return f"uploads/{self.id}/{self.filename}"

    def pull_events(self) -> list[DomainEvent]:
        events = list(self._events)
        self._events.clear()
        return events
