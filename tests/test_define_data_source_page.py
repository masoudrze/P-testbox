import re
import pytest
from uuid import uuid4
from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from pages.define_data_source_page import DefineDataSourcePage




from core.config import settings

import re
from core.test_data_loader import load_test_data

data_source_data = load_test_data("data_sources.json")

@pytest.fixture
def define_data_source_page(authenticated_page: Page) -> DefineDataSourcePage:
    return DefineDataSourcePage(authenticated_page)




@pytest.mark.parametrize("data",data_source_data["invalid_port_char"],)
def test_define_data_source_invalid_port_char( define_data_source_page: DefineDataSourcePage,data: dict,):
    unique_id = uuid4().hex[:8]
    data_source_title_u = f"{data['data_source_title']}_{unique_id}"
    # Step 3: Fill and submit data_source form
    define_data_source_page.define_data_source(
        data_source_title=data["data_source_title"],
        ip=data["ip"],
        port=data["port"],
        user_name=data["user_name"],
        password=data["password"],
        service_name=data["service_name"],
    )

    expect(
        define_data_source_page.error_message.filter(
            has_text=data["expected"]
        ).first
    ).to_be_visible()

    expect(define_data_source_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$")
    )


@pytest.mark.parametrize("data",data_source_data["invalid_port_num"],)
def test_define_data_source_invalid_port_num( define_data_source_page: DefineDataSourcePage,data: dict,):

    # Step 3: Fill and submit data_source form
    define_data_source_page.define_data_source(
        data_source_title=data["data_source_title"],
        ip=data["ip"],
        port=data["port"],
        user_name=data["user_name"],
        password=data["password"],
        service_name=data["service_name"],
    )

    expect(
        define_data_source_page.error_message.filter(
            has_text=data["expected"]
        ).first
    ).to_be_visible()

    expect(define_data_source_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$")
    )


@pytest.mark.parametrize("data",data_source_data["invalid_ip"],)
def test_define_data_source_invalid_ip( define_data_source_page: DefineDataSourcePage,data: dict,):

    # Step 3: Fill and submit data_source form
    define_data_source_page.define_data_source(
        data_source_title=data["data_source_title"],
        ip=data["ip"],
        port=data["port"],
        user_name=data["user_name"],
        password=data["password"],
        service_name=data["service_name"],
    )

    expect(
        define_data_source_page.error_message.filter(
            has_text=data["expected"]
        ).first
    ).to_be_visible()

    expect(define_data_source_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$")
    )


@pytest.mark.parametrize("data",data_source_data["valid"],)
def test_define_data_source_valid( define_data_source_page: DefineDataSourcePage,data: dict,):

    # Step 3: Fill and submit data_source form
    define_data_source_page.define_data_source(
        data_source_title=data["data_source_title"],
        ip=data["ip"],
        port=data["port"],
        user_name=data["user_name"],
        password=data["password"],
        service_name=data["service_name"],
    )

    expect(
        define_data_source_page.error_message.filter(
            has_text=data["expected"]
        ).first
    ).to_be_visible()

    expect(define_data_source_page.page).to_have_url(
        re.compile(re.escape(data["URL_PATTERN"]) + r"/?$")
    )
