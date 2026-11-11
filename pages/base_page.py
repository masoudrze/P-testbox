from playwright.sync_api import Page

from core.config import settings


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.page.set_default_timeout(
            settings.default_timeout
        )

    def open(self, url: str | None = None):
        self.page.goto(url or settings.base_url)

    def click(self, selector: str):
        self.page.locator(selector).click()

    def type(self, selector: str, value: str):
        self.page.locator(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.page.locator(selector).inner_text()