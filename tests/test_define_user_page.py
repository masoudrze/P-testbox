
import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.define_user_page import DefineUserPage

import re

@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    login = LoginPage(page)
    login.open(base_url)
    return login

def define_user_page(page: Page, base_url: str) -> DefineUserPage:
    defineUser = DefineUserPage(page)
    defineUser.open(base_url)
    return defineUser





def test_login_with_valid_credentials(login_page: LoginPage):
    # Replace with credentials from your test environment.
    username = "masoud"
    password = "123456"

    login_page.login(username, password)

    # This test assumes login completes without OTP.
    # If OTP is required, implement OTP handling first.
    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"),
        timeout=30000
    )

def test_define_user(login_page: LoginPage,define_user_page:DefineUserPage):
    username = "masoud"
    password = "123456"

    login_page.login(username, password)

    first_name="احسان",
    last_name="احسانی",
    national_code="0480747474",
    mobile="09127712038",
    user_name="ehsan",
    password="Aa123456",
    role="cadmin"
    define_user_page.define_user( first_name,last_name,national_code,mobile,user_name,password,role)