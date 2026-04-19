def validate_user_structure(data):
    assert isinstance(data, dict), "User response should be a dictionary"

    required_fields = ["id", "name", "username", "email"]
    for field in required_fields:
        assert field in data, f"Missing field: {field}"

    assert isinstance(data["id"], int), "User id should be int"
    assert isinstance(data["name"], str), "User name should be str"
    assert isinstance(data["username"], str), "Username should be str"
    assert isinstance(data["email"], str), "Email shoud be str"