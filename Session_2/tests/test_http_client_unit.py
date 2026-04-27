import pytest
import requests
from http_client import HttpClient


class DummyResponse:
    pass


def test_http_client_get_builds_full_url_and_uses_default_timeout(monkeypatch):
    captured = {}

    def fake_get(url, **kwargs):
        captured["url"] = url
        captured["kwargs"] = kwargs
        return DummyResponse()
    
    monkeypatch.setattr("http_client.requests.get", fake_get)

    client = HttpClient("https://example.com")

    response = client.get("/posts/1")

    assert captured["url"] == "https://example.com/posts/1"
    assert captured["kwargs"]["timeout"] == 5
    assert isinstance(response, DummyResponse)


def test_get_uses_custom_timeout_when_provided(monkeypatch):
    captured = {}

    def fake_get(url, **kwargs):
        captured["url"] = url
        captured["kwargs"] = kwargs
        return DummyResponse()
    
    monkeypatch.setattr("http_client.requests.get", fake_get)

    client = HttpClient("https://api.example.com")

    response = client.get("/users", timeout=10)

    assert captured["url"] == "https://api.example.com/users"
    assert captured["kwargs"]["timeout"] == 10
    assert isinstance(response, DummyResponse)


def test_get_propagates_timeout_exception(monkeypatch):
    def fake_get(url, **kwargs):
        raise requests.Timeout("Request timed out")
    
    monkeypatch.setattr("http_client.requests.get", fake_get)

    client = HttpClient("https://api.example.com")

    with pytest.raises(requests.Timeout):
        client.get("/users")