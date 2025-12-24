
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils import config


class HomePage(BasePage):

    # Search
    SEARCH_INPUT = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SEARCH_SUGGESTIONS = (By.XPATH, '//ul[contains(@class,"_1sFryS _2x2Mmc")]//li')
    SEARCH_ERROR = (By.XPATH,'//div[@class="HG1nJV"]//div')

    # Navigation
    FLIPKART_LOGO = (By.XPATH, '//img[@title="Flipkart"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@title="Login"]')
    CART = (By.XPATH,'//a[@title="Cart"]')
    BECOME_A_SELLER = (By.XPATH,'//a[@title="Become a Seller"]')
    DROP_DOWN = (By.XPATH,'//img[@alt="Dropdown with more help links"]')

    # Categories
    MINUTES_LINK = (By.XPATH,'//*[@aria-label="Minutes"]')
    MOBILES_TABLETS_LINK = (By.XPATH,'//*[@aria-label="Mobiles & Tablets"]')
    FASHION_LINK = (By.XPATH, "//*[@aria-label='Fashion']")
    ELECTRONICS_LINK = (By.XPATH, "//*[@aria-label='Electronics']")
    HOME_KITCHEN_LINK = (By.XPATH,'//*[contains(text(),"Home ")]')
    TVS_APPLIANCES_LINK = (By.XPATH, '//*[@aria-label="TVs & Appliances"]')
    FLIGHT_BOOKINGS_LINK = (By.XPATH,'//*[@aria-label="Flight Bookings"]')
    BEAUTY_TOYS_LINK = (By.XPATH,'//*[contains(text(),"Beauty")]')
    GROCERY_LINK = (By.XPATH,'//*[@aria-label="Grocery"]')
    # FURNITURE_LINK = (By.XPATH,'//a[@aria-label="Furniture"]')

    #pop up
    LOGIN_POP_UP = (By.XPATH,'//span[@role="button"]')

# ==================== PAGE METHODS ====================

    def __init__(self, driver):
        super().__init__(driver)
        self.url = config.BASE_URL

    def open_homepage(self):
        self.open_url(self.url)

    def is_homepage_loaded(self):
        return self.is_element_visible(self.MINUTES_LINK) or self.is_element_visible(self.GROCERY_LINK)

    def close_pop_up(self):
        self.click(self.LOGIN_POP_UP)

    # ==================== SEARCH METHODS ====================

    def search_product(self, product_name):
        self.enter_text(self.SEARCH_INPUT, product_name)
        self.click(self.SEARCH_BUTTON)

    def search_product_with_enter(self, product_name):
        search_box = self.find_element(self.SEARCH_INPUT)
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

    # ==================== NAVIGATION METHODS ====================

    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)

    def is_login_button_clickable(self):
        return self.is_element_clickable(self.LOGIN_BUTTON)

    def click_cart_button(self):
        self.click(self.CART)

    def is_cart_button_visible_and_clickable(self):
        return self.is_element_clickable(self.CART)

    def click_dropdown(self):
        self.click(self.DROP_DOWN)

    def is_drop_down_visible_and_clickable(self):
        return self.is_element_clickable(self.DROP_DOWN)

    def click_logo(self):
        self.click(self.FLIPKART_LOGO)

    # ==================== CATEGORY NAVIGATION ====================

    def is_category_element_visible(self,locator):
        return self.is_element_clickable(locator)

    # ==================== CATEGORY CLICK METHODS ====================

    def click_minutes(self):
        self.click(self.MINUTES_LINK)

    def click_mobiles_tablets(self):
        self.click(self.MOBILES_TABLETS_LINK)

    def click_tvs_appliances(self):
        self.click(self.TVS_APPLIANCES_LINK)

    def click_electronics(self):
        self.click(self.ELECTRONICS_LINK)

    def click_fashion(self):
        self.click(self.FASHION_LINK)

    def click_home_kitchen(self):
        self.click(self.HOME_KITCHEN_LINK)

    def click_beauty_toys(self):
        self.click(self.BEAUTY_TOYS_LINK)

    # def click_furniture(self):
    #     self.click(self.FURNITURE_LINK)
    #     print("furniture button clicked")

    def click_flight_bookings(self):
        self.click(self.FLIGHT_BOOKINGS_LINK)

    def click_grocery(self):
        self.click(self.GROCERY_LINK)


    #===================== search box methods =============================================
    def enter_text_into_search(self,text):
         self.enter_text(self.SEARCH_INPUT,text)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def search_error_message(self):
        return self.get_text(self.SEARCH_ERROR)