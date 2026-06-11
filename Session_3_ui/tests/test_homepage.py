from playwright.sync_api import Page, expect
from Session_3_ui.test_data import HOMEPAGE_HEADING, LEARN_MORE_TEXT, LEARN_MORE_HREF


def test_homepage_heading_is_visible(homepage: Page):
    expect(homepage.get_by_role("heading", name=HOMEPAGE_HEADING)).to_be_visible()


def test_learn_more_link_is_visible_and_points_to_iana(homepage: Page):
    learn_more_link = homepage.get_by_role("link", name=LEARN_MORE_TEXT)

    expect(learn_more_link).to_be_visible()
    expect(learn_more_link).to_be_enabled()

    href = learn_more_link.get_attribute("href")

    assert href is not None, "Learn more link should have an href attribute"
    assert href == LEARN_MORE_HREF, f"Expected href to be {LEARN_MORE_HREF}, but got {href}"


def test_homepage_title_is_correct(homepage: Page):
    expect(homepage).to_have_title("Example Domain")