from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Login form elements
    MOBILE_EMAIL_INPUT = (By.XPATH, '//input[contains(@class,"c3Bd2c yXUQVt")]')
    REQUEST_OTP_BUTTON = (By.XPATH, '//button[text()="Request OTP"]')
    OTP_INPUT = (By.XPATH,'//div[@class="IvbYJ2"]//div')
    VERIFY_OTP_BUTTON = (By.XPATH, '//button[text()="Verify"]')
    RESEND_OTP_LINK = (By.XPATH, '//*[text()="Resend code"]')
    CHANGE_NUMBER = (By.LINK_TEXT,'//a[text()="Change"]')
    CREATE_ACCOUNT_LINK = (By.XPATH, "//a[text()='New to Flipkart? Create an account']")
    EXISTING_USER_LINK = (By.XPATH,'//span[text()="Existing User? Log in"]')

    # Terms and conditions
    TERMS_LINK = (By.XPATH, "//a[text()='Terms of Use']")
    PRIVACY_LINK = (By.XPATH, "//a[text()='Privacy Policy']")

    # Error messages
    INVALID_EMAIL_OR_MOBILE_ERROR = (By.XPATH, '//span[text()="Please enter valid Email ID/Mobile number"]')
    OTP_INVALID_ERROR = (By.XPATH,"//div[text()='OTP is incorrect']")
    # ==================== PAGE METHODS ====================
    def is_login_page_displayed(self):
        return self.is_element_present(self.MOBILE_EMAIL_INPUT)

    def enter_mobile_or_email(self, mobile_email):
        """Enter mobile number or email"""
        self.enter_text(self.MOBILE_EMAIL_INPUT, mobile_email)
        print(f"Entered mobile/email: {mobile_email}")

    def get_error_message(self):
        return self.get_text(self.INVALID_EMAIL_OR_MOBILE_ERROR)
    def is_verify_button_displayed(self):
        return self.is_element_visible(self.VERIFY_OTP_BUTTON)

    def click_request_otp_button(self):
        """Click the login submit button"""
        self.click(self.REQUEST_OTP_BUTTON)
        print("Clicked request otp button")

    def verify_otp(self):
        """Click verify OTP button"""
        self.click(self.VERIFY_OTP_BUTTON)

    def click_create_account(self):
        """Click create new account link"""
        self.click(self.CREATE_ACCOUNT_LINK)

    def is_create_account_page_displayed(self):
        return self.is_element_visible(self.EXISTING_USER_LINK)