import re
import pytest

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.define_role_page import DefineRolePage



@pytest.fixture
def define_role_page(authenticated_page: Page) -> DefineRolePage:
    return DefineRolePage(authenticated_page)



def test_define_role(define_role_page: DefineRolePage):


    # Step 3: Fill and submit role form
    define_role_page.define_role(role_name="تست تعریف نقش 2")
    # expect(define_role_page.error_message).to_have_text(
    #     'کاربر با موفقیت ایجاد شد.'
    # )

    expect(
        define_role_page.error_message.filter(
            has_text="عملیات با موفقیت انجام شد"
        ).first
    ).to_be_visible()