from playwright.sync_api import Page, Locator
from pages.base_page import BasePage


class OTPPage(BasePage):
    def __init__(self, page: Page) -> None:
        super().__init__(page)

        self.otp_inputs: Locator = page.locator("input[name^='otp-']")

        self.submit: Locator = page.get_by_role("button", name="تایید", exact=True)

    def enter_otp(self, otp: str) -> None:
        if len(otp) != 6 or not otp.isdigit():
            raise ValueError("OTP must contain 6 digits")

        for index, digit in enumerate(otp):
            self.page.locator(f"input[name='otp-{index}']").fill(digit)

        self.submit.click()

    def prompt_otp(self) -> None:
        otp = self.page.evaluate("() => window.prompt('Enter OTP:')")

        if otp is None:
            raise ValueError("OTP entry cancelled")

        self.enter_otp(otp)
