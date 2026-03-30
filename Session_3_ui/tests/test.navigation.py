import pytest
from playwright.sync_api import Page, expect
from test_data import LEARN_MORE_TEXT, IANA_HEADING


@pytest.mark.parametrize(
    "link_text, expected_heading",
    [
        (LEARN_MORE_TEXT, IANA_HEADING)
    ]
)
def test_learn_more_link_redirects_to_iana(homepage: Page, link_text, expected_heading):
    homepage.get_by_text(link_text).click()
    homepage.wait_for_url("**iana.org**")
    expect(homepage.get_by_role("heading", name=expected_heading)).to_be_visible()