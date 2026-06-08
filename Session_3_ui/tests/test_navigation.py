import pytest
from playwright.sync_api import Page, expect
from Session_3_ui.test_data import LEARN_MORE_TEXT, IANA_HEADING, HOMEPAGE_HEADING
from Session_3_ui.config import BASE_URL


@pytest.mark.parametrize(
    "link_text, expected_url, expected_heading",
    [
        (LEARN_MORE_TEXT, "https://www.iana.org/help/example-domains", IANA_HEADING)
    ]
)
def test_learn_more_link_redirects_to_iana(homepage: Page, link_text, expected_url, expected_heading):
    homepage.get_by_role("link", name=link_text).click()
    expect(homepage).to_have_url(expected_url)
    expect(homepage.get_by_role("heading", name=expected_heading)).to_be_visible()


def test_user_can_return_to_homepage_after_learn_more_navigation(homepage: Page):
    learn_more_link = homepage.get_by_role("link", name=LEARN_MORE_TEXT)

    expect(learn_more_link).to_be_visible()

    learn_more_link.click()

    expect(homepage).to_have_url("https://www.iana.org/help/example-domains")

    homepage.go_back()

    expect(homepage).to_have_url(BASE_URL)
    expect(homepage.get_by_role("heading", name=HOMEPAGE_HEADING)).to_be_visible()