import pytest
from playwright.sync_api import Page, expect
from core.config import settings
from pages.login_page import LoginPage
import re
from core.test_data_loader import load_test_data

login_data = load_test_data("login.json")


@pytest.mark.parametrize("data",login_data["short_password"],)
def test_login_with_short_password(login_page: LoginPage,data: dict,):
    login_page.login(
        user_name=data["user_name"],
        password=data["password"],
        )

    expect(login_page.error_message).to_have_text(
        "password:مطمعن شوید طول این مقدار حداقل 6 است."
    )
    expect(login_page.page).to_have_url(re.compile(r".*/auth/login/?$"))

@pytest.mark.parametrize("data",login_data["invalid_credentials"],)
def test_login_with_invalid_credentials(login_page: LoginPage,data: dict,):
    login_page.login(
        user_name=data["user_name"],
        password=data["password"],
        )

    expect(login_page.error_message).to_have_text(
        "نام کاربری یا کلمه عبور اشتباه می باشد"
    )
    expect(login_page.page).to_have_url(re.compile(r".*/auth/login/?$"))


def test_login_with_valid_credentials(login_page: LoginPage):
    # Replace with credentials from your test environment.


    login_page.login(settings.test_username, settings.test_password)

    # expect(login_page.error_message).to_have_text("با موفقیت وارد شدید", timeout=30000)

    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"), timeout=30000
    )


def test_forgot_password_navigation(login_page: LoginPage):
    login_page.navigate_forgot_password()

    expect(login_page.page).to_have_url(re.compile(r".*/auth/forget-password/?$"))
