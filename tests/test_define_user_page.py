import re
import pytest

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.define_user_page import DefineUserPage

@pytest.fixture
def define_user_page(authenticated_page: Page) -> DefineUserPage:
    return DefineUserPage(authenticated_page)


def test_define_user(define_user_page: DefineUserPage):

    # Step 3: Fill and submit user form
    define_user_page.define_user(
        first_name="احسان8",
        last_name="احسانی8",
        national_code="0480747482",
        mobile="09127712038",
        user_name="ehsan8",
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
