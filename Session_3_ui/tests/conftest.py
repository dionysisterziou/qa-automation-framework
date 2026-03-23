import pytest
from config import BASE_URL


@pytest.fixture
def homepage(page):
  page.goto(BASE_URL)
  return page