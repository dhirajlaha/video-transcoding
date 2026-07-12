from dataclasses import dataclass
from uuid import UUID

from pydantic import BaseModel, Field

from backend.application.ports import PresignedUploadService
from backend.domain.video import Video


class CreateUploadCommand(BaseModel):
    filename: str = Field(min_length=1)
    content_type: str = Field(min_length=1)


@dataclass(frozen=True, slots=True)
class CreateUploadResult:
    video_id: UUID
    upload_url: str
    object_key: str


@dataclass(frozen=True, slots=True)
class CreateUpload:
    upload_service: PresignedUploadService

    def execute(self, command: CreateUploadCommand) -> CreateUploadResult:
        video = Video.create_upload(filename=command.filename, content_type=command.content_type)
        upload_url = self.upload_service.create_upload_url(video)
        return CreateUploadResult(
            video_id=video.id,
            upload_url=upload_url,
            object_key=video.object_key,
        )
