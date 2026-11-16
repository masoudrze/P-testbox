import pytest
from playwright.sync_api import Page, expect

from pages.login_page import LoginPage

import re
from pages.menu_page import MenuPage



@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    login = LoginPage(page)
    login.open()
    return login

@pytest.fixture
def menu_page(page: Page) -> MenuPage:
    return MenuPage(page)



def test_navigate_menu_pages_dashboard(login_page: LoginPage, menu_page: MenuPage):

    login_page.login("masoud", "123456")

    # Step 2: Wait for dashboard
    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"),
        timeout=120000
    )

    # menu_page.navigate_dashboard()
    menu_page.navigate_organization_reports()

    expect(login_page.page).to_have_url(
        re.compile(r".*/admin/dashboardoo/?$"),
        timeout=120000
    )
