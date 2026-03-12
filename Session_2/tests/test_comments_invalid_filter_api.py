def test_get_comments_invalid_filter_api(client_get):
    response = client_get("/comments?postId=abc")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)
    assert data == []