def validate_comment_structure(comment):
    assert isinstance(comment, dict), "Comment must be a dict"

    # contract
    assert "postId" in comment, "Missing field: postId"
    assert "id" in comment, "Missing field: id"
    assert "name" in comment, "Missing field: name"
    assert "email" in comment, "Missing field: email"
    assert "body" in comment, "Missing field: body"

    # type
    assert isinstance(comment["postId"], int), "postId must be int"
    assert isinstance(comment["id"], int), "id must be int"
    assert isinstance(comment["name"], str), "name must be str"
    assert isinstance(comment["email"], str), "email must be str"
    assert isinstance(comment["body"], str), "body must be str"

    # meaningful value
    assert comment["id"], "id must not be empty"
    assert comment["name"], "name must not be empty"
    assert comment["email"], "email must not be empty"
    assert comment["body"], "body must not be empty"

    # light sanity
    assert "@" in comment["email"], "email must contain @"


def validate_comment(comment, expected_post_id):
    validate_comment_structure(comment)
    assert comment["postId"] == expected_post_id, (
        f"Expected postId {expected_post_id}, got {comment['postId']}"
    )


def validate_comment_by_id(comment, expected_id):
    validate_comment_structure(comment)
    assert comment["id"] == expected_id, (
        f"Expected comment id {expected_id}, got {comment['id']}"
    )