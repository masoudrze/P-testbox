import re
import pytest

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.define_data_source_page import DefineDataSourcePage


@pytest.fixture
def define_data_source_page(authenticated_page: Page) -> DefineDataSourcePage:
    return DefineDataSourcePage(authenticated_page)





def test_define_data_source( define_data_source_page: DefineDataSourcePage
):

    # Step 3: Fill and submit data_source form
    define_data_source_page.define_data_source(
        data_source_title="تست منبع داده 2",
        ip="192.168.1.2",
        port="1234",
        user_name="testuser2",
        password="123456",
        service_name="source test 2",
    )

    expect(
        define_data_source_page.error_message.filter(
            has_text="منبع داده با موفقیت ایجاد شد."
        ).first
    ).to_be_visible()

    # expect(define_role_page.page).to_have_url(
    # re.compile(r".*/list/?$"),
    # timeout=30000
    # )
