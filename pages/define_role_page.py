from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class DefineRolePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Locators
        self.title: Locator = page.locator("input[name='title']")

        self.submit: Locator = page.locator("button[type='submit']")

        self.error_message: Locator = page.locator(
            "div[role='alert'][aria-describedby='notistack-snackbar']"
        )

    def define_role(
        self,
        role_name: str,
    ) -> None:
        """Enter user info and submit the define user form."""

        self.open("/admin/role/create")
        self.title.fill(role_name)
        self.submit.click()

    def get_error_message(self) -> str:
        """Return the displayed login error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Check whether the login error is visible."""
        return self.error_message.is_visible()
