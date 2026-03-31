import pytest
import requests


class HttpClient:
    def __init__(self, base_url):
        self.base_url = base_url

    
    def get(self, path, **kwargs):
        full_url = self.base_url + path
        kwargs.setdefault("timeout", 5)
        return requests.get(full_url, **kwargs)


def parse_json(response):
    try:
        return response.json()
    except Exception:
        pytest.fail(f"Response is not valid JSON: {response.text}")