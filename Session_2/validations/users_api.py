def validate_user_1(data):
    assert data["id"] == 1, f"Expected id=1, got {data['id']}"
    assert "username" in data, "Username does not exist"
    assert "email" in data, "Email does not exist"