import requests


def test_get_post_1_status_code():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")

    assert response.status_code == 200, "Status code should be 200"