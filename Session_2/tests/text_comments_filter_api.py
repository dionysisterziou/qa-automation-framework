import pytest
from validations.post_comments_api import validate_comment

@pytest.mark.parametrize(
    "post_id",
    [1, 2]
)
def test_get_comments_filter_api(client_get, post_id):
    response = client_get(f"/comments?postId={post_id}")

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    data = response.json()

    assert isinstance(data, list), f"Expected list, got {type(data)}"
    assert data, "Empty list"

    for comment in data:
        validate_comment(comment, post_id)