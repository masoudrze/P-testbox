import re
import pytest

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.define_data_source_page import DefineDataSourcePage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login


@pytest.fixture
def define_data_source_page(page: Page) -> DefineDataSourcePage:
    return DefineDataSourcePage(page)


def test_define_data_source(
    login_page: LoginPage,
    define_data_source_page: DefineDataSourcePage
):
    # Step 1: Login
    login_page.login("masoud", "123456")

    # Step 2: Wait for dashboard
    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"),
        timeout=120000
    )



    # Step 3: Fill and submit data_source form
    define_data_source_page.define_data_source(
        data_source_title="تست منبع داده 1",
        ip="192.168.1.1",
        port="1234",
        user_name="testuser1",
        password="123456",
        service_name="source test 1"
    )


    expect(define_data_source_page.error_message.filter(
        has_text="منبع داده با موفقیت ایجاد شد."
        ).first
    ).to_be_visible()


    # expect(define_role_page.page).to_have_url(
    # re.compile(r".*/list/?$"),
    # timeout=30000
    # )
