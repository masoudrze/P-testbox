
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Locators
        self.first_name: Locator = page.locator(
            "input[name='first_name']"
        )
        self.last_name: Locator = page.locator(
            "input[name='last_name']"
        )

        self.national_code: Locator = page.locator(
            "input[name='national_code']"
        )

        self.mobile: Locator = page.locator(
            "input[name='mobile']"
        )

        self.user_name: Locator = page.locator(
            "input[name='user_name']"
        )

        self.password: Locator = page.locator(
            "input[name='password']"
        )

        self.role: Locator = page.locator(
            "input[name='role']"
        )



        self.error_message: Locator = page.locator(
            "div[role='alert'][aria-describedby='notistack-snackbar']"
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
