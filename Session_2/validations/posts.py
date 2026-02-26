def validate_post_1(data):
    assert data["id"] == 1, "Post id should be 1"
    assert data["userId"] == 1, "User id should be 1"