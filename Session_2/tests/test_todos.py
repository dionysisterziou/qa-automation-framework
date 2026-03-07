import pytest
from validations.todos_api import validate_todo_by_id


@pytest.mark.parametrize(
    "todo_id",
    [1, 2]
)
def test_get_todo_by_id_ok(client_get, todo_id):
    response = client_get(f"/todos/{todo_id}")
    assert response.status_code == 200, f"Expected response to be 200, got {response.status_code}"

    data = response.json()
    validate_todo_by_id(data, todo_id)