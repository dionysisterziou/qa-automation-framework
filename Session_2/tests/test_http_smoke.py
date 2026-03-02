import requests
import pytest
from validations.posts import validate_post_1
from http_client import get


def test_get_post_1_status_code():
    response = get("/posts/1")
    assert response.status_code == 200, "Status code should be 200"


def test_get_post_1_body_fields():
    response = get("/posts/1")
    data = response.json()

    validate_post_1(data)


def test_get_post_1_wrong_expectation_should_fail():
    response = get("/posts/1")
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
    response = get(f"/posts/{post_id}")
    assert response.status_code == 200, "Status code should be 200"


def test_get_post_invalid_id_returns_404():
    response = get("/posts/0")
    assert response.status_code == 404, "Status code should be 404"


def test_get_post_invalid_endpoint_returns_404():
    response = get("/invalid_endpoint")
    assert response.status_code == 404, f"Unexpected status code: {response.status_code}"

# Μάθημα 11: Timeouts
def test_timeout_should_raise_exception():
    with pytest.raises(requests.exceptions.Timeout):
        get("/posts/1", timeout=0.0001)


# Μάθημα 12: Invalid JSON (JSON decode error)
def test_response_json_on_plain_text_should_fail():
    response = requests.get("https://httpbin.org/html", timeout=5)
    assert response.status_code == 200, f"Unexpected status code: {response.status_code}"

    with pytest.raises(ValueError):
        response.json()


def test_https_ssl_failure_should_raise():
    with pytest.raises(requests.exceptions.SSLError):
        requests.get("https://example.com", timeout=5)


# Μάθημα 13: Redirects (301/302) με requests
def test_redirect_302_has_location_header():
    response = requests.get("https://httpbin.org/redirect/1", allow_redirects=False, timeout=5)

    assert response.status_code in (301, 302), f"Expected redirect, got {response.status_code}"
    assert "Location" in response.headers, "Redirect response should include Location header"


# Μάθημα 14: Redirect followed vs not followed (behaviour check)
def test_redirect_is_followed_by_default():
    response = requests.get("https://httpbin.org/redirect/1", timeout=5)

    assert response.status_code == 200, f"Expected final 200, got {response.status_code}"
    assert len(response.history) == 1, f"Expected 1 redirect, got {len(response.history)}"
    assert response.history[0].status_code in (301, 302), "History should contain redirect response"