# conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from webdriver_manager.chrome import ChromeDriverManager

from pages.home_page import HomePage
from utils import config  # Make sure you have this config file


# ==================== BROWSER FIXTURES ====================

@pytest.fixture(params=["chrome"])
def driver(request):
    browser = request.param
    print(f"\nInitializing {browser} browser...")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)

    yield driver
    driver.quit()


@pytest.fixture(params=["chrome"], scope="class")
def driver1(request):
    browser = request.param
    print(f"\nInitializing {browser} browser for class scope...")

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if config.HEADLESS:
            options.add_argument("--headless")
        options.add_argument("--start-maximized")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")

        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)
    driver.maximize_window()

    yield driver
    driver.quit()


# ==================== PAGE FIXTURES ====================

@pytest.fixture
def home(driver):
    home = HomePage(driver)
    home.open_homepage()
    try:
        home.close_pop_up()
    finally:
        return home



# # ==================== HOOK: AUTOMATIC SCREENSHOTS ====================
#
# import os
# from datetime import datetime
#
# # Add this import at the top if you're using pytest-html
# try:
#     from pytest_html import extras
# except ImportError:
#     extras = None
#
#
# @pytest.hookimpl(hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Automatically takes screenshot on test failure for both driver and driver1 fixtures
#     """
#     outcome = yield  # Let pytest run the test
#     report = outcome.get_result()  # Get test result after test finishes
#
#     # Only take screenshot if test failed during execution
#     if report.when == 'call' and report.failed:
#         # Try both driver fixtures
#         driver = item.funcargs.get('driver') or item.funcargs.get('driver1')
#
#         if driver:
#             # Create screenshots directory
#             os.makedirs('screenshots', exist_ok=True)  # Fixed directory name
#
#             # Generate unique filename
#             timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
#             screenshot_name = f"{item.name}_{timestamp}.png"
#             screenshot_path = f"screenshots/{screenshot_name}"  # Fixed path
#
#             # Take and save screenshot
#             try:
#                 driver.save_screenshot(screenshot_path)
#                 print(f"\n📸 Screenshot saved: {screenshot_path}")
#
#                 # Attach to pytest-html report if available
#                 if extras and os.path.exists(screenshot_path):
#                     extra = getattr(report, 'extra', [])
#                     extra.append(extras.image(screenshot_path))
#                     report.extra = extra
#             except Exception as e:
#                 print(f"⚠️ Failed to take screenshot: {str(e)}")