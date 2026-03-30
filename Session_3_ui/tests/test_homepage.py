from playwright.sync_api import Page, expect
from test_data import  HOMEPAGE_HEADING


def test_homepage_has_expected_title(homepage: Page):
    expect(homepage.get_by_role("heading", name=HOMEPAGE_HEADING)).to_be_visible()