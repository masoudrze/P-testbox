import re
import pytest
from uuid import uuid4

from playwright.sync_api import Page, expect
from pages.define_data_source_page import DefineDataSourcePage
from core.test_data_loader import load_test_data


data_source_data = load_test_data("data_sources.json")


test_cases = [
    pytest.param(data, id=f"{category}_{index}")
    for category, items in data_source_data.items()
    for index, data in enumerate(items, start=1)
]


@pytest.fixture
def define_data_source_page(authenticated_page: Page) -> DefineDataSourcePage:
    return DefineDataSourcePage(authenticated_page)


@pytest.mark.parametrize("data",test_cases)

def test_define_data_source(
    define_data_source_page: DefineDataSourcePage,
    data: dict,
):

    define_data_source_page.define_data_source(
        data_source_title=data["data_source_title"],
        ip=data["ip"],
        port=data["port"],
        user_name=data["user_name"],
        password=data["password"],
        service_name=data["service_name"],
    )

    expect(
        define_data_source_page.error_message.filter(has_text=data["expected"]).first
    ).to_be_visible()

    expect(define_data_source_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$")
    )
