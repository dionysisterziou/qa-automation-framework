def validate_todo_by_id(data, expected_id):
    
    # id
    assert "id" in data, "Missing 'id'"
    assert isinstance(data["id"], int), f"Expected int, got {type(data['id'])}"
    assert data["id"] == expected_id, f"Expected 'id' to be {expected_id}, got {data['id']}"

    # userId
    assert "userId" in data, "Missing 'userId'"
    assert isinstance(data["userId"], int), f"Expected 'userId' to be int, got {type(data['userId'])}"
    assert data["userId"], "'userId' is empty"

    # title
    assert "title" in data, "Missing 'title'"
    assert isinstance(data["title"], str), f"Expected 'title' to be str, got {type(data['title'])}"
    assert data["title"], "'title' is empty"

    # completed
    assert "completed" in data, "Missing 'completed'"
    assert isinstance(data["completed"], bool), f"Expected 'completed' to be bool, got {type(data['completed'])}"