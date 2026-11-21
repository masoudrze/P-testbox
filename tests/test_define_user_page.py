import pytest

from playwright.sync_api import Page, expect
from pages.define_user_page import DefineUserPage
from core.test_data_loader import load_test_data

user_data = load_test_data("users.json")


@pytest.fixture
def define_user_page(authenticated_page: Page) -> DefineUserPage:
    return DefineUserPage(authenticated_page)


@pytest.mark.parametrize(
    "data",
    user_data["valid"],
)
def test_define_user(define_user_page: DefineUserPage, data: dict):

    # Step 3: Fill and submit user form
    define_user_page.define_user(
        first_name=data["first_name"],
        last_name=data["last_name"],
        national_code=data["national_code"],
        mobile=data["mobile"],
        user_name=data["user_name"],
        password=data["password"],
        role_name=data["role_name"],
    )

    expect(
        define_user_page.error_message.filter(has_text=data["expected"]).first
    ).to_be_visible()

    expect(
        define_user_page.error_message.filter(has_text="کاربر با موفقیت ایجاد شد").first
    ).to_be_visible()
