from fastapi import FastAPI

from backend.application.use_cases import CreateUpload, CreateUploadCommand
from backend.config.settings import Settings
from backend.infrastructure.storage import LocalPresignedUploadService

settings = Settings()
upload_service = LocalPresignedUploadService(settings=settings)
create_upload = CreateUpload(upload_service=upload_service)

app = FastAPI(title="Video Transcoding Platform", version="0.1.0")


@app.get("/health", tags=["system"])
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/videos/uploads", tags=["videos"])
def create_video_upload(command: CreateUploadCommand) -> dict[str, str]:
    upload = create_upload.execute(command)
    return {
        "video_id": str(upload.video_id),
        "upload_url": upload.upload_url,
        "object_key": upload.object_key,
    }
