import requests


def test_get_post_1_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200, "Status code should be 200"


def test_get_post_1_body_fields():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()

    assert data["id"] == 1, "ID should be 1"
    assert data["userId"] == 1, "User ID should be 1"