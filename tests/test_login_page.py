import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

import re
from pages.otp_page import OTPPage


@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login


def test_login_with_short_password(login_page: LoginPage):
    login_page.login("test", "test")

    expect(login_page.error_message).to_have_text(
        "password:مطمعن شوید طول این مقدار حداقل 6 است."
    )
    expect(login_page.page).to_have_url(re.compile(r".*/auth/login/?$"))


def test_login_with_invalid_credentials(login_page: LoginPage):
    login_page.login("test", "test123456")

    expect(login_page.error_message).to_have_text(
        "نام کاربری یا کلمه عبور اشتباه می باشد"
    )
    expect(login_page.page).to_have_url(re.compile(r".*/auth/login/?$"))


def test_login_with_valid_credentials(login_page: LoginPage):
    # Replace with credentials from your test environment.
    username = "masoud"
    password = "123456"

    login_page.login(username, password)
    # Step 2: Wait for OTP page
    # otp_page = OTPPage(login_page.page)
    # otp_page.page.wait_for_url("**/auth/enter-code")
    # # Step 3: Enter OTP manually
    # otp_page.prompt_otp()
    # This test assumes login completes without OTP.
    # If OTP is required, implement OTP handling first.

    expect(login_page.error_message).to_have_text("با موفقیت وارد شدید.", timeout=30000)

    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"), timeout=30000
    )


def test_forgot_password_navigation(login_page: LoginPage):
    login_page.navigate_forgot_password()

    expect(login_page.page).to_have_url(re.compile(r".*/auth/forget-password/?$"))
