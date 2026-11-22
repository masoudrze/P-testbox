import pytest
from playwright.sync_api import Page, expect
from core.config import settings
from pages.forget_password_page import ForgetPasswordPage
import re
from core.test_data_loader import load_test_data

forget_password_data = load_test_data("forget_password.json")

@pytest.fixture
def forget_password_page(page: Page) -> ForgetPasswordPage:
    forget = ForgetPasswordPage(page)
    forget.open()
    return forget


test_cases = [
    pytest.param(data, id=f"{category}_{index}")
    for category, items in forget_password_data.items()
    for index, data in enumerate(items, start=1)
]


@pytest.mark.parametrize("data",test_cases,)
def test_forget_password(
    forget_password_page: ForgetPasswordPage,
    data: dict,
):
    forget_password_page.forget_password(
        user_name=data["user_name"],
        mobile=data["mobile"],
    )

    expect(
        forget_password_page.error_message.filter(has_text=data["expected"]).first
    ).to_be_visible()

    expect(forget_password_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$"), timeout=30000
    )






def test_login_page_navigation(forget_password_page: ForgetPasswordPage):
    forget_password_page.navigate_login_page()

    expect(forget_password_page.page).to_have_url(re.compile(r".*/auth/login/?$"))
