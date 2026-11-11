
from playwright.sync_api import Page, Locator, expect

from core.config import settings


class BasePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.page.set_default_timeout(settings.default_timeout)

    def open(self, url: str | None = None) -> None:
        self.page.goto(url or settings.base_url)

    def find(self, selector: str) -> Locator:
        return self.page.locator(selector)

    def click(self, selector: str) -> None:
        self.find(selector).click()

    def type(self, selector: str, value: str) -> None:
        self.find(selector).fill(value)

    def get_text(self, selector: str) -> str:
        return self.find(selector).inner_text()

    def wait_until_visible(self, selector: str) -> None:
        expect(self.find(selector)).to_be_visible()

    def wait_until_hidden(self, selector: str) -> None:
        expect(self.find(selector)).to_be_hidden()

    def is_visible(self, selector: str) -> bool:
        return self.find(selector).is_visible()

    def hover(self, selector: str) -> None:
        self.find(selector).hover()

    def get_attribute(
        self, selector: str, attribute: str
    ) -> str | None:
        return self.find(selector).get_attribute(attribute)

    def get_url(self) -> str:
        return self.page.url
