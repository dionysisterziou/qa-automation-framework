import pytest
from http_client import parse_json
from validations.posts_api import validate_post_by_id
from validations.posts_api import validate_post_for_user


def test_get_post_by_id_ok(client_get):
    response = client_get("/posts/1")

    assert response.status_code == 200

    data = parse_json(response)

    validate_post_by_id(data, 1)


def test_get_post_missing_resource(client_get):
    response = client_get("/posts/999999")

    assert response.status_code == 404

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_for_user_ok(client_get, user_id):
    response = client_get(f"/users/{user_id}/posts")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data

    for post in data:
        validate_post_for_user(post, user_id)


@pytest.mark.parametrize("user_id", [1, 2])
def test_get_posts_filter_by_user_ok(client_get, user_id):
    response = client_get(f"/posts?userId={user_id}")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data

    for post in data:
        validate_post_for_user(post, user_id)


def test_get_posts_filter_by_user_empty_result(client_get):
    response = client_get("/posts?userId=999999")

    assert response.status_code == 200

    data = parse_json(response)

    assert isinstance(data, list)
    assert data == []