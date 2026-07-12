from urllib.parse import quote

from backend.config.settings import Settings
from backend.domain.video import Video


class LocalPresignedUploadService:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def create_upload_url(self, video: Video) -> str:
        object_key = quote(video.object_key)
        return f"{self._settings.s3_endpoint_url}/{self._settings.s3_bucket}/{object_key}"
