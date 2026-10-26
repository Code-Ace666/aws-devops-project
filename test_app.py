import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_index(client):
    res = client.get("/")
    assert res.status_code == 200
    assert res.get_json() == {"message": "Hello, Flask!"}


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json() == {"status": "ok"}


def test_greet(client):
    res = client.post("/greet", json={"name": "Ada"})
    assert res.status_code == 200
    assert res.get_json() == {"message": "Hello, Ada!"}


def test_greet_missing_name(client):
    res = client.post("/greet", json={})
    assert res.status_code == 400
    assert "error" in res.get_json()
