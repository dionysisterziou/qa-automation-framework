import pytest
from validations.users_api import validate_user_structure
from http_client import parse_json

@pytest.mark.parametrize(
    "expected_id",
    [
        1,
        2
    ]
)
def test_get_user_by_id_ok(api_client, expected_id):

    response = api_client.get(f"/users/{expected_id}")
    
    assert response.status_code == 200, f"Expected final 200, got {response.status_code}"
    
    data = parse_json(response)

    validate_user_structure(data)
    assert data["id"] == expected_id


def test_get_user_missing_resource(api_client):
    response = api_client.get("/users/999999")

    assert response.status_code == 404

    data = parse_json(response)

    assert data == {}