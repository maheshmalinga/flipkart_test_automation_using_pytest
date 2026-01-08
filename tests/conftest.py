
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options

from pages.home_page import HomePage
from utils import config


# ==================== BROWSER FIXTURES ====================

@pytest.fixture()
def driver():
    options = Options()
    if config.HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    if config.BROWSER == "chrome":
        driver = Chrome(options=options)

    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)

    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def driver1():
    options = Options()
    if config.HEADLESS:
        options.add_argument("--headless")
    options.add_argument("--start-maximized")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-popup-blocking")
    if config.BROWSER == "chrome":
        driver = Chrome(options=options)

    driver.implicitly_wait(config.IMPLICIT_WAIT)
    driver.set_page_load_timeout(config.PAGE_LOAD_TIMEOUT)

    yield driver
    driver.quit()


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
#                 print(f"\nScreenshot saved: {screenshot_path}")
#
#                 # Attach to pytest-html report if available
#                 if extras and os.path.exists(screenshot_path):
#                     extra = getattr(report, 'extra', [])
#                     extra.append(extras.image(screenshot_path))
#                     report.extra = extra
#             except Exception as e:
#                 print(f"Failed to take screenshot: {str(e)}")