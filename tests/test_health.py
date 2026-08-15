"""Tests for health and root endpoints."""


def test_root_endpoint(client):
    """GET / returns API metadata."""
    r = client.get("/")
    assert r.status_code == 200
    data = r.json()
    assert "Plant Disease Detection" in data["message"]
    assert "version" in data
    assert "/predict" in data["endpoints"]
    assert "/chat" in data["endpoints"]
    assert "/health" in data["endpoints"]


def test_health_endpoint(client):
    """GET /health returns healthy status with model loaded."""
    r = client.get("/health")
    assert r.status_code == 200
    data = r.json()
    assert data["status"] == "healthy"
    assert data["model_loaded"] is True
    assert "version" in data


def test_health_model_not_loaded(client, mock_model_service):
    """GET /health reflects model_loaded=False correctly."""
    mock_model_service.model_loaded = False
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["model_loaded"] is False
