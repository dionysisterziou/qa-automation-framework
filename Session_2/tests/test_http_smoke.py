import requests
import pytest
from validations.posts import validate_post_1


def test_get_post_1_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200, "Status code should be 200"


def test_get_post_1_body_fields():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()

    validate_post_1(data)


def test_get_post_1_wrong_expectation_should_fail():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    data["id"] = 999

    with pytest.raises(AssertionError):
        validate_post_1(data)


@pytest.mark.parametrize(
    "post_id",
    [
        1,
        2,
        3
    ]
)
def test_get_posts_status_code_ok(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")

    assert response.status_code == 200, "Status code should be 200"


def test_get_post_invalid_id_returns_404():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/0")

    assert response.status_code == 404, "Status code should be 404"


def test_get_post_invalid_endpoint_returns_404():
    response = requests.get("https://jsonplaceholder.typicode.com/invalid_endpoint")

    assert response.status_code == 404, f"Unexpected status code: {response.status_code}"


def test_timeout_should_raise_exception():
    with pytest.raises(requests.exceptions.Timeout):
        requests.get(
            "https://jsonplaceholder.typicode.com/posts/1",
            timeout=0.0001
        )