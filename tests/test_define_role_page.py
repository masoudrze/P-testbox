import re
import pytest

from playwright.sync_api import Page, expect
from pages.define_role_page import DefineRolePage
from core.test_data_loader import load_test_data

role_data = load_test_data("roles.json")

@pytest.fixture
def define_role_page(authenticated_page: Page) -> DefineRolePage:
    return DefineRolePage(authenticated_page)


@pytest.mark.parametrize(
    "data",
    role_data["valid"],
)
def test_define_role(
    define_role_page: DefineRolePage,
    data: dict,
):
    define_role_page.define_role(
        role_name=data["role_name"]
    )

    expect(
        define_role_page.error_message.filter(
            has_text=data["expected"]
        ).first
    ).to_be_visible()



    



# def test_define_role(define_role_page: DefineRolePage):


#     # Step 3: Fill and submit role form
#     define_role_page.define_role(role_name="تست تعریف نقش 2")
#     # expect(define_role_page.error_message).to_have_text(
#     #     'کاربر با موفقیت ایجاد شد.'
#     # )

#     expect(
#         define_role_page.error_message.filter(
#             has_text="عملیات با موفقیت انجام شد"
#         ).first
#     ).to_be_visible()