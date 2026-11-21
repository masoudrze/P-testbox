import re
import pytest
from core.config import settings

from playwright.sync_api import Browser, Page, expect

from pages.login_page import LoginPage
from collections.abc import Generator


@pytest.fixture(scope="session")
def base_url():
    return settings.base_url


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture(scope="session")
def auth_state(browser: Browser):
    context = browser.new_context()
    try:
        page = context.new_page()

        login = LoginPage(page)
        login.open()
        login.login(settings.test_username, settings.test_password)

        expect(page).to_have_url(re.compile(r".*/admin/dashboard/?$"), timeout=120000)

        return context.storage_state()
    finally:
        context.close()


@pytest.fixture
def authenticated_page(
    browser: Browser, auth_state: dict
) -> Generator[Page, None, None]:

    context = browser.new_context(storage_state=auth_state)

    try:
        page = context.new_page()

        page.goto(f"{settings.base_url.rstrip('/')}/admin/dashboard")

        expect(page).to_have_url(re.compile(r".*/admin/dashboard/?$"))

        yield page
    finally:
        context.close()
