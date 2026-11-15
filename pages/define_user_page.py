
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage

from core.config import settings


class DefineUserPage(BasePage):

    PATH = "/admin/users/create"

    def __init__(self, page: Page) -> None:
        super().__init__(page)


        def open(self) -> None:
            url = f"{settings.base_url.rstrip('/')}{self.PATH}"
            super().open(url)

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

        self.role: Locator = page.get_by_role(
            "combobox",name="نقش *",exact=True
        )

        self.submit: Locator = page.locator(
            "button[type='submit']"
        )

        self.error_message: Locator = page.locator(
            "div[role='alert'][aria-describedby='notistack-snackbar']"
        )

    def select_role(self, role_name: str) -> None:
        option: Locator = self.page.get_by_role(
            "option",
            name=role_name,
            exact=True
        )

        self.select_combobox(self.role, option)

    def define_user(self,
                     first_name: str,
                     last_name: str,
                     national_code: str,
                     mobile: str,
                     user_name: str,
                     password: str,
                     role: str,) -> None:
        """Enter user info and submit the define user form."""
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.national_code.fill(national_code)
        self.mobile.fill(mobile)
        self.user_name.fill(user_name)
        self.password.fill(password)
        self.role.click()
        self.select_combobox(self.role,role)
        self.submit.click()

    def select_role(self, role_name: str) -> None:
        self.role.click()

        self.page.get_by_role(
            "option",
            name=role_name,
            exact=True
        ).click()

    def get_error_message(self) -> str:
        """Return the displayed login error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Check whether the login error is visible."""
        return self.error_message.is_visible()
