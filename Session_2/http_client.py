import requests
from config import BASE_URL


def get(path, **kwargs):
    full_url = BASE_URL + path
    kwargs.setdefault("timeout", 5)
    return requests.get(full_url, **kwargs)