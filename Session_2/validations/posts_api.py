def validate_post_structure(post):
    # shape
    assert isinstance(post, dict), "Post must be a dict"

    # contract
    assert "userId" in post, "Missing field: userId"
    assert "id" in post, "Missing field: id"
    assert "title" in post, "Missing field: title"
    assert "body" in post, "Missing field: body"

    # type
    assert isinstance(post["userId"], int), "userId must be int"
    assert isinstance(post["id"], int), "id must be int"
    assert isinstance(post["title"], str), "title must be str"
    assert isinstance(post["body"], str), "body must be str"

    # meaningful value
    assert post["userId"] > 0, "userId must be greater than 0"
    assert post["id"] > 0, "id must be greater than 0"
    assert post["title"], "title must not be empty"
    assert post["body"], "body must not be empty"


# context
def validate_post_by_id(post, expected_id):
    validate_post_structure(post)

    assert post["id"] == expected_id, (
        f"Expected post id {expected_id}, got {post['id']}"
    )


def validate_post_for_user(post, expected_user_id):
    validate_post_structure(post)

    assert post["userId"] == expected_user_id, (
        f"Expected userId {expected_user_id}, got {post['userId']}"
    )