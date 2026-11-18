import re
import pytest

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.define_role_page import DefineRolePage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def define_role_page(page: Page) -> DefineRolePage:
    return DefineRolePage(page)


def test_define_role(login_page: LoginPage, define_role_page: DefineRolePage):
    # Step 1: Login
    login_page.login("masoud", "123456")

    # Step 2: Wait for dashboard
    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"), timeout=120000
    )

    # Step 3: Fill and submit role form
    define_role_page.define_role(role_name="تست تعرف نقش 1")
    # expect(define_role_page.error_message).to_have_text(
    #     'کاربر با موفقیت ایجاد شد.'
    # )

    expect(
        define_role_page.error_message.filter(
            has_text="عملیات با موفقیت انجام شد"
        ).first
    ).to_be_visible()

    # expect(define_role_page.page).to_have_url(
    # re.compile(r".*/list/?$"),
    # timeout=30000
    # )
