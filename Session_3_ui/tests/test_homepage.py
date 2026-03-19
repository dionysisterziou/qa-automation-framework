from playwright.sync_api import Page


def test_homepage_has_expected_title(page: Page):
    page.goto("https://example.com")

    assert page.title() == "Example Domain"
    assert page.get_by_text("Example Domain").is_visible()


def test_homepage_link_redirects(page: Page):
    page.goto("https://example.com")
    page.get_by_text("More information...").click()
    page.wait_for_url("**iana.org**")

    assert "iana.org" in page.url