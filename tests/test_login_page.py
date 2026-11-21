import pytest
from playwright.sync_api import Page, expect
from core.config import settings
from pages.login_page import LoginPage
import re
from core.test_data_loader import load_test_data

login_data = load_test_data("login.json")

test_cases = [
    pytest.param(data, id=f"{category}_{index}")
    for category, items in login_data.items()
    for index, data in enumerate(items, start=1)
]


@pytest.mark.parametrize("data",test_cases,)
def test_login(
    login_page: LoginPage,
    data: dict,
):
    login_page.login(
        user_name=data["user_name"],
        password=data["password"],
    )

    expect(
        login_page.error_message.filter(has_text=data["expected"]).first
    ).to_be_visible()

    expect(login_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$")
    )



@pytest.mark.parametrize(
    "data",
    login_data["valid"],
)
def test_login_with_valid_credentials(
    login_page: LoginPage,
    data: dict,
):
    # Replace with credentials from your test environment.

    login_page.login(settings.test_username, settings.test_password)

    expect(login_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$"), timeout=30000
    )

    expect(
        login_page.error_message.filter(has_text=data["expected"]).first
    ).to_be_visible()


def test_forgot_password_navigation(login_page: LoginPage):
    login_page.navigate_forgot_password()

    expect(login_page.page).to_have_url(re.compile(r".*/auth/forget-password/?$"))
