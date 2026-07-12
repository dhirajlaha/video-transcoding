from fastapi.testclient import TestClient

from apps.api.main import app


def test_health() -> None:
    client = TestClient(app)
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_video_upload() -> None:
    client = TestClient(app)
    response = client.post(
        "/videos/uploads",
        json={"filename": "sample.mp4", "content_type": "video/mp4"},
    )

    assert response.status_code == 200
    body = response.json()
    assert body["video_id"]
    assert body["object_key"].endswith("/sample.mp4")
    assert body["upload_url"].startswith("http://localhost:9000/videos/uploads/")
