"""
Helper functions for the test framework
"""

import json
import os
from datetime import datetime

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def load_test_data(file_path="test_data/test_data.json"):
    """Load test data from JSON file"""
    with open(file_path, 'r') as file:
        return json.load(file)


def take_screenshot(driver, name):
    """Take screenshot and save with timestamp"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    screenshot_name = f"screenshots/{name}_{timestamp}.png"

    # Create directory if not exists
    os.makedirs("screenshots", exist_ok=True)

    driver.save_screenshot(screenshot_name)
    print(f"Screenshot saved: {screenshot_name}")
    return screenshot_name


def wait_for_element(driver, locator, timeout=15):
    """Wait for element to be visible"""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.visibility_of_element_located(locator))


def wait_for_element_clickable(driver, locator, timeout=15):
    """Wait for element to be clickable"""
    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.element_to_be_clickable(locator))


def scroll_to_element(driver, element):
    """Scroll to bring element into view"""
    driver.execute_script("arguments[0].scrollIntoView(true);", element)


def scroll_page(driver, pixels=500):
    """Scroll page by specified pixels"""
    driver.execute_script(f"window.scrollBy(0, {pixels});")


def get_current_timestamp():
    """Get current timestamp for unique identifiers"""
    return datetime.now().strftime("%Y%m%d%H%M%S")