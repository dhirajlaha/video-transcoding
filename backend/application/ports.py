from typing import Protocol

from backend.domain.video import Video


class PresignedUploadService(Protocol):
    def create_upload_url(self, video: Video) -> str: ...
