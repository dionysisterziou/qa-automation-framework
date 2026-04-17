from http_client import parse_json
from validations.posts_api import validate_post_structure


def test_create_post_ok(api_client):
    payload = {
        "title": "my test title",
        "body": "my test body",
        "userId": 1,
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201

    data = parse_json(response)

    validate_post_structure(data)
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]


def test_create_post_missing_body_does_not_match_full_post_contract(api_client):
    payload = {
        "title": "my test title",
        "userId": 1,
    }

    response = api_client.post("/posts", json=payload)

    assert response.status_code == 201

    data = parse_json(response)

    assert isinstance(data, dict)
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]
    assert "body" not in data