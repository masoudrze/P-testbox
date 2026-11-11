
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Locators
        self.username: Locator = page.locator(
            "input[name='username']"
        )

        self.password: Locator = page.locator(
            "input[name='password']"
        )

        self.submit: Locator = page.locator(
            "button[type='submit']"
        )

        self.forgot_password_link: Locator = page.locator(
            "a[href='/auth/forget-password']"
        )

        self.error_message: Locator = page.locator(
            "div[role='alert']"
        )

    def login(self, username: str, password: str) -> None:
        """Enter credentials and submit the login form."""
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()

    def forgot_password(self) -> None:
        """Navigate to the forgot password page."""
        self.forgot_password_link.click()

    def get_error_message(self) -> str:
        """Return the displayed login error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Check whether the login error is visible."""
        return self.error_message.is_visible()
