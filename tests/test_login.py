
import pytest
from pages.home_page import HomePage
from pages.login_page import LoginPage

@pytest.fixture
def home_page(driver):
    home_page = HomePage(driver)
    home_page.open_homepage()
    home_page.click_login_button()
    return home_page

@pytest.fixture
def login(driver):
    login_page = LoginPage(driver)
    return login_page

@pytest.mark.smoke
def test_is_login_page_displayed(driver, home_page,login):
    assert login.is_login_page_displayed(), "Login page is not displayed"
@pytest.mark.smoke
def test_is_enter_email_phone_field_displayed(driver, home_page,login):
    assert login.enter_mobile_or_email_field_clickable()
@pytest.mark.smoke
def test_is_request_otp_button_displayed(driver, home_page,login):
    assert login.is_request_otp_button_displayed()
@pytest.mark.smoke
def test_is_terms_link_displayed(driver, home_page,login):
    assert login.is_terms_link_displayed()
@pytest.mark.smoke
def test_is_privacy_link_displayed(driver, home_page,login):
    assert login.is_privacy_link_displayed()
@pytest.mark.smoke
def test_is_create_account_link_displayed(driver, home_page,login):
    assert login.is_create_account_link_displayed()
def test_click_terms_link(driver, home_page,login):
    login.click_terms_link()
    driver.switch_to.window(driver.window_handles[1])
    assert "terms" in driver.current_url
def test_click_privacy_link(driver, home_page,login):
    login.click_terms_link()
    driver.switch_to.window(driver.window_handles[1])
    assert "privacy" in driver.current_url
def test_click_create_account_link(driver, home_page,login):
    login.click_create_account()
    assert "account" in driver.current_url

@pytest.mark.smoke
def test_click_request_otp_button(driver, home_page,login):
    login.enter_mobile_or_email("9391575398")
    login.click_request_otp_button()
    assert login.is_verify_button_displayed()

@pytest.mark.smoke
@pytest.mark.regression
def test_login_with_valid_10_digit_mobile(driver,home_page,login):
    login.enter_mobile_or_email("9391575398")
    login.click_request_otp_button()
    assert login.is_verify_button_displayed(), "Valid phone format not accepted"

@pytest.mark.smoke
@pytest.mark.regression
def test_login_with_empty_mobile_number(driver, home_page,login):
    login.click_request_otp_button()
    assert login.get_error_message() in 'Please enter valid Email ID/Mobile number','No validation shown for empty fields'

@pytest.mark.regression
def test_login_with_invalid_mobile_format(driver, home_page,login):
    login.enter_mobile_or_email("12345")
    login.click_request_otp_button()
    assert login.get_error_message() == 'Please enter valid Email ID/Mobile number','No validation shown for empty fields'


@pytest.mark.regression
def test_login_with_valid_email_format(driver, home_page,login):
    login.enter_mobile_or_email("test@example.com")
    login.click_request_otp_button()
    assert login.is_verify_button_displayed(), "Valid email format not accepted"

@pytest.mark.regression
def test_login_with_uppercase_email(driver, home_page, login):
    login.enter_mobile_or_email("TEST@EXAMPLE.COM")
    login.click_request_otp_button()
    assert login.is_verify_button_displayed()

@pytest.mark.regression
def test_login_with_invalid_email(driver, home_page, login):
    login.enter_mobile_or_email("abcd@.com")
    login.click_request_otp_button()
    assert login.get_error_message() == 'Please enter valid Email ID/Mobile number'

@pytest.mark.regression
def test_create_account_link(driver, home_page,login):
    login.click_create_account()
    assert login.is_existing_user_button_clickable()

def test_is_existing_user_button_displayed(driver, home_page,login):
    login.click_create_account()
    login.is_existing_user_button_clickable()



