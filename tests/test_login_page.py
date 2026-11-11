from playwright.sync_api import Page, expect

from pages.login_page import LoginPage


def test_invalid_login(page: Page, base_url):
    login_page = LoginPage(page)

    login_page.open(base_url)

    login_page.login(
        "invalid_user",
        "invalid_password"
    )

    expect(
        page.locator("button[type='submit']")
    ).to_be_visible()