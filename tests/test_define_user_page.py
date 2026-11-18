import re
import pytest

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.define_user_page import DefineUserPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def define_user_page(page: Page) -> DefineUserPage:
    return DefineUserPage(page)


def test_define_user(login_page: LoginPage, define_user_page: DefineUserPage):
    # Step 1: Login
    login_page.login("masoud", "123456")

    # Step 2: Wait for dashboard
    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"), timeout=120000
    )

    # Step 3: Fill and submit user form
    define_user_page.define_user(
        first_name="احسان7",
        last_name="احسانی7",
        national_code="0480747481",
        mobile="09127712038",
        user_name="ehsan7",
        password="Aa123456",
        role_name="cadmin",
    )
    # expect(define_user_page.error_message).to_have_text(
    #     'کاربر با موفقیت ایجاد شد.'
    # )

    expect(
        define_user_page.error_message.filter(has_text="کاربر با موفقیت ایجاد شد").first
    ).to_be_visible()

    # expect(define_user_page.page).to_have_url(
    # re.compile(r".*/list/?$"),
    # timeout=30000
    # )
