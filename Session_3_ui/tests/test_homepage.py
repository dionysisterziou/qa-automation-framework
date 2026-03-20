from playwright.sync_api import Page, expect


def test_homepage_has_expected_title(homepage: Page):
    assert homepage.title() == "Example Domain"
    expect(homepage.get_by_role("heading", name="Example Domain")).to_be_visible()


def test_homepage_link_redirects(homepage: Page):
    homepage.get_by_text("Learn more").click()
    homepage.wait_for_url("**iana.org**")

    assert "iana.org" in homepage.url