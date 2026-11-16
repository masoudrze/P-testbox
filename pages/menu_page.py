
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class MenuPage(BasePage):

    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # Locators
        self.dashboard: Locator = page.locator(
            "a[href='/admin/dashboard']"
        )

        self.role_access_management: Locator = page.get_by_role(
            "button", name="مديريت نقش و دسترسي"
        )

        self.organization_reports_access_management: Locator = page.get_by_role(
            "button", name="گزارشات سازماني"
        )

        self.organization_reports_page: Locator = page.get_by_role(
            "link", name="مشاهده گزارش"
        )


        self.username: Locator = page.locator(
            "input[name='username']"
        )


        self.error_message: Locator = page.locator(
            "div[role='alert'][aria-describedby='notistack-snackbar']"
        )

    def navigate_dashboard(self) -> None:
        """Navigate to the dashboard page."""
        self.dashboard.click()

    def navigate_organization_reports(self) -> None:
        """Navigate to the organization reports page."""
        self.organization_reports_access_management.hover()
        self.organization_reports_page.click()

    def get_error_message(self) -> str:
        """Return the displayed login error message."""
        return self.error_message.inner_text()

    def is_error_visible(self) -> bool:
        """Check whether the login error is visible."""
        return self.error_message.is_visible()
