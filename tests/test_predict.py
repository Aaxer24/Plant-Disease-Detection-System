"""Tests for the prediction endpoint."""

import io

from PIL import Image


def _make_image() -> bytes:
    """Create a minimal green PNG for upload tests."""
    img = Image.new("RGB", (256, 256), color=(34, 139, 34))
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)
    return buf.read()


def test_predict_valid_image(client, mock_mlflow_service):
    """POST /predict with a valid image returns a prediction response."""
    r = client.post(
        "/predict",
        files={"file": ("leaf.png", _make_image(), "image/png")},
    )
    assert r.status_code == 200
    data = r.json()
    assert data["class_name"] == "Potato___healthy"
    assert data["display_name"] == "Healthy"
    assert data["confidence"] == 98.5
    assert "all_predictions" in data
    assert "disease_info" in data
    mock_mlflow_service.log_prediction.assert_called_once()


def test_predict_invalid_file_type(client):
    """POST /predict with a non-image file returns HTTP 400."""
    r = client.post(
        "/predict",
        files={"file": ("data.txt", b"not an image", "text/plain")},
    )
    assert r.status_code == 400
    assert "image" in r.json()["detail"].lower()


def test_predict_model_error(client, mock_model_service):
    """POST /predict returns HTTP 500 when the model raises."""
    mock_model_service.predict.side_effect = RuntimeError("model not loaded")
    r = client.post(
        "/predict",
        files={"file": ("leaf.png", _make_image(), "image/png")},
    )
    assert r.status_code == 500
    assert "failed" in r.json()["detail"].lower()
