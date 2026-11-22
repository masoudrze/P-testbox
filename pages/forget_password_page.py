from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class ForgetPasswordPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Locators
        self.username: Locator = page.locator("input[name='username']")

        self.mobile: Locator = page.locator("input[name='mobile']")

        self.submit: Locator = page.locator("button[type='submit']")

        self.forgot_password_link: Locator = page.locator(
            "a[href='/auth/forget-password']"
        )

        self.login_page_link: Locator = page.locator(
            "a[href='/auth/login']"
        )

        # self.error_message: Locator = page.locator(
        #     "div[role='alert'][aria-describedby='notistack-snackbar']"
        # )
        self.error_message: Locator = page.locator(".notistack-MuiContent-error")

        # self.error_message = page.locator(".notistack-MuiContent-error")

    def forget_password(self, user_name: str, mobile: str) -> None:
        """Enter credentials and submit the login form."""
        # self.forgot_password_link.click()
        self.mobile.fill(mobile)
        self.username.fill(user_name)
        self.submit.click()

    def navigate_login_page(self) -> None:
        """Navigate to the forgot password page."""
        self.login_page_link.click()

    def get_error_message(self) -> str:
        """Return the displayed login error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Check whether the login error is visible."""
        return self.error_message.is_visible()
