import re

import pytest
from playwright.sync_api import Browser, Page, expect

from pages.login_page import LoginPage
from pages.menu_page import MenuPage


# @pytest.fixture
# def login_page(page: Page, base_url: str) -> LoginPage:
#     login = LoginPage(page)
#     login.open()
#     return login

# @pytest.fixture
# def menu_page(page: Page) -> MenuPage:
#     return MenuPage(page)


@pytest.fixture(scope="module")
def authenticated_page(
    browser: Browser,
    base_url: str
):
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open()
    login_page.login("masoud", "123456")

    expect(page).to_have_url(
        re.compile(r".*/admin/dashboard/?$"),
        timeout=120000
    )

    yield page

    context.close()


@pytest.fixture
def menu_page(authenticated_page: Page) -> MenuPage:
    return MenuPage(authenticated_page)

#################



# def test_navigate_organization_reports(
#     login_page: LoginPage,
#     menu_page: MenuPage
# ):
#     login_page.login("masoud", "123456")

#     expect(login_page.page).to_have_url(
#         re.compile(r".*/admin/dashboard/?$"),
#         timeout=120000
#     )

#     menu_page.navigate_reports_management_menu_define()

#     expect(menu_page.page).to_have_url(
#         re.compile(r".*/admin/reports/create/?$")
#     )

#     menu_page.navigate_reports_management_menu_list()

#     expect(menu_page.page).to_have_url(
#         re.compile(r".*/admin/reports/?$")
#     )

#     menu_page.navigate_organization_reports_management_menu()

#     expect(menu_page.page).to_have_url(
#         re.compile(r".*/admin/organizationreports/?$")
#     )
# مشاهده داشبورد

def test_navigate_dashboard(menu_page: MenuPage):
    menu_page.navigate_dashboard()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/dashboard/?$")
    )

#   مديريت کاربران

def test_navigate_users_management_menu_define(menu_page: MenuPage):
    menu_page.navigate_users_management_menu_define()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/users/create/?$")
    )

def test_navigate_users_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_users_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/users/?$")
    )

#    مديريت نقش و دسترسي

def test_navigate_roles_management_menu_define(menu_page: MenuPage):
    menu_page.navigate_roles_management_menu_define()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/role/create/?$")
    )

def test_navigate_roles_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_roles_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/role/?$")
    )

def test_navigate_roles_columns_limit_management_menu_define(menu_page: MenuPage):
    menu_page.navigate_roles_columns_limit_management_menu_define()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/role/column-limits/create/?$")
    )

def test_navigate_roles_columns_limit_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_roles_columns_limit_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/role/column-limits/?$")
    )

#  مديريت منابع داده

def test_navigate_data_sources_management_menu_define(menu_page: MenuPage):
    menu_page.navigate_data_sources_management_menu_define()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/sources/create/?$")
    )

def test_navigate_data_sources_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_data_sources_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/sources/?$")
    )

#  پايش رويداد ها (لاگ سيستم)

def test_navigate_auditlogs_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_auditlogs_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/auditlogs/?$")
    )

#  مديريت دسته بندي گزارشات

def test_navigate_reports_category_management_menu_define(menu_page: MenuPage):
    menu_page.navigate_reports_category_management_menu_define()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/reportcategories/create/?$")
    )

def test_navigate_reports_category_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_reports_category_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/reportcategories/?$")
    )

#  مدیریت گزارشات

def test_navigate_reports_management_menu_define(menu_page: MenuPage):
    menu_page.navigate_reports_management_menu_define()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/reports/create/?$")
    )

def test_navigate_reports_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_reports_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/reports/?$")
    )

# گزارشات سازمانی

def test_navigate_organization_reports_management_menu_list(menu_page: MenuPage):
    menu_page.navigate_organization_reports_management_menu_list()

    expect(menu_page.page).to_have_url(
        re.compile(r".*/admin/organizationreports/?$")
    )
