def validate_user(user):
    assert user["role"] == "admin", "User must be admin"
    assert user["active"], "User must be active"