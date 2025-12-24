from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from utils import config

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, config.EXPLICIT_WAIT)
        self.actions = ActionChains(driver)

    # ==================== BASIC ACTIONS ====================

    def open_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def refresh_page(self):
        self.driver.refresh()

    def go_back(self):
        self.driver.back()

    def go_forward(self):
        self.driver.forward()

#==================== ELEMENT INTERACTIONS ====================#

    def is_element_present(self, locator,timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_visible(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        return element.text

    # ==================== ADVANCED ACTIONS ====================

    def hover_over_element(self, locator):
        element = self.driver.find_element(locator)
        self.actions.move_to_element(element).perform()
        print(f"Hovered over element: {locator}")

    def double_click(self, locator):
        element = self.driver.driver.driver.find_element(locator)
        self.actions.double_click(element).perform()

    def right_click(self, locator):
        element = self.driver.find_element(locator)
        self.actions.context_click(element).perform()

    def drag_and_drop(self, source_locator, target_locator):
        source = self.driver.find_element(source_locator)
        target = self.driver.find_element(target_locator)
        self.actions.drag_and_drop(source, target).perform()

    def scroll_to_element(self, locator):
        element = self.driver.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def scroll_page(self, pixels=500):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")

    # ==================== JAVASCRIPT METHODS ====================

    def js_click(self, locator):
        element = self.driver.find_element(locator)
        self.driver.execute_script("arguments[0].click();", element)
        print(f"JS clicked on element: {locator}")

    def js_enter_text(self, locator, text):
        element = self.driver.find_element(locator)
        self.driver.execute_script(f"arguments[0].value = '{text}';", element)

    def highlight_element(self, locator):
        element = self.driver.find_element(locator)
        self.driver.execute_script(
            "arguments[0].style.border='3px solid red'", element
        )

    # ==================== SCREENSHOT ====================

    def take_screenshot(self, name):
        """Take screenshot"""
        from utils.helpers import take_screenshot
        return take_screenshot(self.driver, name)

    # ==================== ALERTS ====================

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.accept()

    def dismiss_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert.dismiss()

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        return alert.text

    # ==================== WINDOW HANDLING ====================

    def switch_to_window(self, window_index):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[window_index])

    def switch_to_new_window(self):
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

    def close_current_window(self):
        self.driver.close()

    def get_window_count(self):
        return len(self.driver.window_handles)

    # ==================== IFRAME HANDLING ====================

    def switch_to_frame(self, locator):
        frame = self.driver.find_element(locator)
        self.driver.switch_to.frame(frame)

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()