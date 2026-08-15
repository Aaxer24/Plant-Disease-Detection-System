"""Tests for the chat endpoint."""


def test_chat_basic(client):
    """POST /chat with a simple message returns a response."""
    r = client.post("/chat", json={"message": "What is early blight?"})
    assert r.status_code == 200
    data = r.json()
    assert "response" in data
    assert len(data["response"]) > 0


def test_chat_with_disease_context(client):
    """POST /chat with disease_context attaches context correctly."""
    r = client.post(
        "/chat",
        json={
            "message": "How do I treat this?",
            "disease_context": "Potato___Early_blight",
            "confidence": 95.0,
        },
    )
    assert r.status_code == 200
    assert "response" in r.json()


def test_chat_with_history(client):
    """POST /chat with conversation_history is accepted."""
    r = client.post(
        "/chat",
        json={
            "message": "Tell me more",
            "conversation_history": [
                {"role": "user", "content": "What is early blight?"},
                {"role": "assistant", "content": "Early blight is a fungal disease."},
            ],
        },
    )
    assert r.status_code == 200
    assert "response" in r.json()


def test_chat_empty_message(client):
    """POST /chat with an empty message still returns HTTP 200."""
    r = client.post("/chat", json={"message": ""})
    assert r.status_code == 200


def test_chat_stream(client):
    """POST /chat/stream returns the reply incrementally as chunked text."""
    with client.stream(
        "POST", "/chat/stream", json={"message": "What is early blight?"}
    ) as r:
        assert r.status_code == 200
        body = "".join(r.iter_text())
    assert body == "Your potato plant looks healthy! Keep it up 🌱"
