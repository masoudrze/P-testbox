from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

        self.username = page.locator(
            "input[name='username']"
        )

        self.password = page.locator(
            "input[name='password']"
        )

        self.submit = page.locator(
            "button[type='submit']"
        )

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()