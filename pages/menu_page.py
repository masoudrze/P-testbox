from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class MenuPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        # مشاهده داشبورد

        self.dashboard: Locator = page.locator("a[href='/admin/dashboard']")

        #   مديريت کاربران

        self.users_management_menu: Locator = page.get_by_role(
            "button", name="مديريت کاربران"
        )

        self.users_define_page: Locator = page.get_by_role(
            "link", name="ثبت نام کاربر جديد", exact=True
        )

        self.users_list_page: Locator = page.get_by_role(
            "link", name="مشاهده ليست کاربران", exact=True
        )

        #    مديريت نقش و دسترسي

        self.roles_management_menu: Locator = page.get_by_role(
            "button", name="مديريت نقش و دسترسي", exact=True
        )

        self.roles_define_page: Locator = page.get_by_role(
            "link", name="ثبت نقش جديد", exact=True
        )

        self.roles_list_page: Locator = page.get_by_role(
            "link", name="مشاهده ليست نقش ها", exact=True
        )

        self.columns_limit_define_page: Locator = page.get_by_role(
            "link", name="ثبت محدوديت سر ستون گزارش", exact=True
        )

        self.columns_limit_list_page: Locator = page.get_by_role(
            "link", name="مشاهده ليست محدوديت سر ستون گزارش", exact=True
        )

        #  مديريت منابع داده

        self.data_sources_management_menu: Locator = page.get_by_role(
            "button", name="مديريت منابع داده", exact=True
        )

        self.data_sources_define_page: Locator = page.get_by_role(
            "link", name="ثبت منبع داده جديد", exact=True
        )

        self.data_sources_list_page: Locator = page.get_by_role(
            "link", name="مشاهده ليست منابع داده", exact=True
        )

        #  پايش رويداد ها (لاگ سيستم)

        self.auditlogs_management_menu: Locator = page.get_by_role(
            "button", name="پايش رويداد ها (لاگ سيستم)", exact=True
        )

        self.auditlogs_list_page: Locator = page.get_by_role(
            "link", name="مشاهده فهرست رويداد ها", exact=True
        )

        #  مديريت دسته بندي گزارشات

        self.reports_category_management_menu: Locator = page.get_by_role(
            "button", name="مديريت دسته بندي گزارشات", exact=True
        )

        self.reports_category_define_page: Locator = page.get_by_role(
            "link", name="ثبت دسته بندي گزارش جديد", exact=True
        )

        self.reports_category_list_page: Locator = page.get_by_role(
            "link", name="مشاهده ليست دسته بندي گزارش ها", exact=True
        )

        #  مدیریت گزارشات

        self.reports_management_menu: Locator = page.get_by_role(
            "button", name="مديريت گزارشات", exact=True
        )

        self.reports_define_page: Locator = page.get_by_role(
            "link", name="ثبت گزارش جديد", exact=True
        )

        self.reports_list_page: Locator = page.get_by_role(
            "link", name="مشاهده ليست گزارش ها", exact=True
        )

        # گزارشات سازمانی

        self.organization_reports_management_menu: Locator = page.get_by_role(
            "button", name="گزارشات سازماني", exact=True
        )

        self.organization_reports_list_page: Locator = page.get_by_role(
            "link", name="مشاهده گزارش", exact=True
        )

        self.username: Locator = page.locator("input[name='username']")

        self.error_message: Locator = page.locator(
            "div[role='alert'][aria-describedby='notistack-snackbar']"
        )

    # مشاهده داشبورد

    def navigate_dashboard(self) -> None:
        """Navigate to the dashboard page."""
        self.dashboard.click()

    #   مديريت کاربران

    def navigate_users_management_menu_define(self) -> None:
        self.hover_and_click(self.users_management_menu, self.users_define_page)

    def navigate_users_management_menu_list(self) -> None:
        self.hover_and_click(self.users_management_menu, self.users_list_page)

    #    مديريت نقش و دسترسي

    def navigate_roles_management_menu_define(self) -> None:
        self.hover_and_click(self.roles_management_menu, self.roles_define_page)

    def navigate_roles_management_menu_list(self) -> None:
        self.hover_and_click(self.roles_management_menu, self.roles_list_page)

    def navigate_roles_columns_limit_management_menu_define(self) -> None:
        self.hover_and_click(self.roles_management_menu, self.columns_limit_define_page)

    def navigate_roles_columns_limit_management_menu_list(self) -> None:
        self.hover_and_click(self.roles_management_menu, self.columns_limit_list_page)

    #  مديريت منابع داده

    def navigate_data_sources_management_menu_define(self) -> None:
        self.hover_and_click(
            self.data_sources_management_menu, self.data_sources_define_page
        )

    def navigate_data_sources_management_menu_list(self) -> None:
        self.hover_and_click(
            self.data_sources_management_menu, self.data_sources_list_page
        )

    #  پايش رويداد ها (لاگ سيستم)

    def navigate_auditlogs_management_menu_list(self) -> None:
        self.hover_and_click(self.auditlogs_management_menu, self.auditlogs_list_page)

    #  مديريت دسته بندي گزارشات

    def navigate_reports_category_management_menu_define(self) -> None:
        self.hover_and_click(
            self.reports_category_management_menu, self.reports_category_define_page
        )

    def navigate_reports_category_management_menu_list(self) -> None:
        self.hover_and_click(
            self.reports_category_management_menu, self.reports_category_list_page
        )

    #  مدیریت گزارشات

    def navigate_reports_management_menu_define(self) -> None:
        self.hover_and_click(self.reports_management_menu, self.reports_define_page)

    def navigate_reports_management_menu_list(self) -> None:
        self.hover_and_click(self.reports_management_menu, self.reports_list_page)

    # گزارشات سازمانی

    def navigate_organization_reports_management_menu_list(self) -> None:
        self.hover_and_click(
            self.organization_reports_management_menu,
            self.organization_reports_list_page,
        )
