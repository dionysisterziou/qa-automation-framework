import pytest
from Session_3_ui.config import BASE_URL


@pytest.fixture
def homepage(page):
  page.goto(BASE_URL)
  return page