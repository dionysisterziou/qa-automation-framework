import requests
import pytest


def test_get_post_1_status_code(api_client):
    response = api_client.get("/posts/1")
    assert response.status_code == 200, "Status code should be 200"


@pytest.mark.parametrize(
    "post_id",
    [
        1,
        2,
        3
    ]
)
def test_get_posts_status_code_ok(api_client, post_id):
    response = api_client.get(f"/posts/{post_id}")
    assert response.status_code == 200


def test_get_post_invalid_id_returns_404(api_client):
    response = api_client.get("/posts/0")
    assert response.status_code == 404, "Status code should be 404"


def test_get_post_invalid_endpoint_returns_404(api_client):
    response = api_client.get("/invalid_endpoint")
    assert response.status_code == 404, f"Unexpected status code: {response.status_code}"


def test_timeout_should_raise_exception(api_client):
    with pytest.raises(requests.exceptions.Timeout):
        api_client.get("/posts/1", timeout=0.0001)