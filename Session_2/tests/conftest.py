import pytest
from http_client import HttpClient
from config import BASE_URL


@pytest.fixture
def api_client():
    return HttpClient(BASE_URL)