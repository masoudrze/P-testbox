import pytest
from uuid import uuid4
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
    unique_id = uuid4().hex[:8]
    role_name_u = f"{data['role_name']}_{unique_id}"
    define_role_page.define_role(role_name=role_name_u)

    expect(
        define_role_page.error_message.filter(has_text=data["expected"]).first
    ).to_be_visible()

