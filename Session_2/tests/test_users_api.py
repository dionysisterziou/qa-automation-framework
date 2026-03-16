import pytest
from validations.users_api import validate_user_by_id

@pytest.mark.parametrize(
    "expected_id",
    [
        1,
        2
    ]
)
def test_get_user_by_id_ok(client_get, expected_id):
    response = client_get(f"/users/{expected_id}") # timeout=5 μπαίνει default από http_client
    data = response.json()

    assert response.status_code == 200, f"Expected final 200, got {response.status_code}"
    validate_user_by_id(data, expected_id)


def test_get_user_missing_resource(client_get):
    response = client_get("/users/999999")

    assert response.status_code == 404

    data = response.json()
    assert data == {}