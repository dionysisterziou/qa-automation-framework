from http_client import get
from validations.users_api import validate_user_1


def test_get_user_1_status_code_ok():
    response = get("/users/1", timeout=5)

    assert response.status_code == 200, f"Expected final 200, got {response.status_code}"


def test_get_user_1_body_fields():
    response = get("/users/1", timeout=5)

    validate_user_1(response.json())