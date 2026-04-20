import pytest
from validations.todos_api import validate_todo_structure
from http_client import parse_json


@pytest.mark.parametrize(
    "expected_id",
    [1, 2]
)
def test_get_todo_by_id_ok(api_client, expected_id):
    response = api_client.get(f"/todos/{expected_id}")

    assert response.status_code == 200

    data = parse_json(response)

    validate_todo_structure(data)
    assert data["id"] == expected_id