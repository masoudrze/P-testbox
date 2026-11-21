from playwright.sync_api import Page, Locator

from pages.base_page import BasePage

from core.config import settings


class DefineDataSourcePage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Locators
        self.data_source_title: Locator = page.locator(
            "input[name='data_source_title']"
        )

        self.ip: Locator = page.locator("input[name='ip']")

        self.port: Locator = page.locator("input[name='port']")

        self.user_name: Locator = page.locator("input[name='user_name']")

        self.password: Locator = page.locator("input[name='password']")

        self.service_name: Locator = page.locator("input[name='service_name']")

        self.submit: Locator = page.locator("button[type='submit']")

        # self.error_message: Locator = page.locator(
        #     "div[role='alert'][aria-describedby='notistack-snackbar']"
        # )

        self.error_message: Locator = page.get_by_role("alert")

    def define_data_source(
        self,
        data_source_title: str,
        ip: str,
        port: str,
        user_name: str,
        password: str,
        service_name: str,
    ) -> None:
        """Enter user info and submit the define user form."""

        self.open("/admin/sources/create")
        self.data_source_title.fill(data_source_title)
        self.ip.fill(ip)
        self.port.fill(port)
        self.user_name.fill(user_name)
        self.password.fill(password)
        self.service_name.fill(service_name)
        self.submit.click()

    def get_error_message(self) -> str:
        """Return the displayed login error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Check whether the login error is visible."""
        return self.error_message.is_visible()
