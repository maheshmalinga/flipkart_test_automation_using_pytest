
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
from utils import config


class HomePage(BasePage):

    # Search
    SEARCH_BAR = (By.NAME, "q")
    SEARCH_BUTTON = (By.XPATH, '//button[@type="submit"]')
    SEARCH_SUGGESTIONS = (By.XPATH, '//ul[contains(@class,"_1sFryS _2x2Mmc")]//li')
    SEARCH_ERROR = (By.XPATH,'//div[@class="HG1nJV"]//div')

    # Navigation
    FLIPKART_LOGO = (By.XPATH, '//img[@title="Flipkart"]')
    LOGIN_BUTTON = (By.XPATH, '//a[@title="Login"]')
    CART = (By.XPATH,'//a[@title="Cart"]/parent::div')
    BECOME_SELLER = (By.XPATH,'//*[text()="Become a Seller"]')
    DROP_DOWN = (By.XPATH,'//img[@alt="Dropdown with more help links"]')

    # Categories
    MINUTES_LINK = (By.XPATH,'//*[@aria-label="Minutes"]')
    MOBILES_TABLETS_LINK = (By.XPATH,'//*[@aria-label="Mobiles & Tablets"]')
    FASHION_LINK = (By.XPATH, "//*[@aria-label='Fashion']")
    ELECTRONICS_LINK = (By.XPATH, "//*[@aria-label='Electronics']")
    HOME_FURNITURE_LINK = (By.XPATH,'//*[contains(text(),"Home ")]')
    TVS_APPLIANCES_LINK = (By.XPATH, '//*[@aria-label="TVs & Appliances"]')
    FLIGHT_BOOKINGS_LINK = (By.XPATH,'//*[@aria-label="Flight Bookings"]')
    BEAUTY_LINK = (By.XPATH,'//*[contains(text(),"Beauty")]')
    GROCERY_LINK = (By.XPATH,'//*[@aria-label="Grocery"]')
    # FURNITURE_LINK = (By.XPATH,'//a[@aria-label="Furniture"]')

    # login drop down elements
    SIGN_UP = (By.XPATH, '//*[@title="Sign Up"]')
    MY_PROFILE  = (By.XPATH, '//*[@title="My Profile"]')
    FLIPKART_PLUS = (By.XPATH, '//*[@tile="Flipkart Plus Zone"]')
    ORDERS = (By.XPATH, '//*[@tile="Orders"]')
    WISH_LIST = (By.XPATH, '//*[@title="Wishlist"]')
    # drop down elements
    NOTIFICATION_PREFERENCES = (By.XPATH, '//*[@title="Notification Preferences"]')
    CUSTOMER_CARE = (By.XPATH, '//*[@title="24x7 Customer Care"]')
    ADVERTISE = (By.XPATH, '//*[@title="Advertise"]')
    DOWNLOAD_APP = (By.XPATH, '//*[@title="Download App"]')
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
        self.enter_text(self.SEARCH_BAR, product_name)
        self.click(self.SEARCH_BUTTON)

    def search_product_with_enter(self, product_name):
        search_box = self.find_element(self.SEARCH_BAR)
        search_box.clear()
        search_box.send_keys(product_name)
        search_box.send_keys(Keys.RETURN)

    # ==================== NAVIGATION METHODS ====================
    def is_logo_button_clickable(self):
        return self.is_element_clickable(self.FLIGHT_BOOKINGS_LINK)

    def click_logo(self):
        self.click(self.FLIPKART_LOGO)
        
    def is_search_bar_clickable(self):
        return self.is_element_clickable(self.SEARCH_BAR)
    
    def is_search_button_clickable(self):
        return self.is_element_clickable(self.SEARCH_BUTTON)

    def click_search_button(self):
        self.click(self.SEARCH_BUTTON)
    #------- login ------------------------

    def is_login_button_clickable(self):
        return self.is_element_clickable(self.LOGIN_BUTTON)
    def hover_over_login(self):
        self.hover_over_element(self.LOGIN_BUTTON)
    def is_sign_up_button_clickable(self):
        return self.is_element_clickable(self.SIGN_UP)
    def is_my_profile_button_clickable(self):
        return self.is_element_clickable(self.MY_PROFILE)
    def is_flipkart_plus_button_clickable(self):
        return self.is_element_clickable(self.FLIPKART_PLUS)
    def is_orders_button_clickable(self):
        return self.is_element_clickable(self.ORDERS)
    def is_wish_list_button_clickable(self):
        return self.is_element_clickable(self.WISH_LIST)
    def is_login_drop_down_displayed(self):
        return self.is_sign_up_button_clickable()
    def click_sign_up(self):
        self.click(self.SIGN_UP)
    def click_my_profile(self):
        self.click(self.MY_PROFILE)
    def click_flipkart_plus(self):
        self.click(self.FLIPKART_PLUS)
    def click_orders(self):
        self.click(self.ORDERS)
    def click_wish_list(self):
        self.click(self.WISH_LIST)
    def click_login_button(self):
        self.click(self.LOGIN_BUTTON)
    # -------------- cart -----------------------
    def is_cart_button_clickable(self):
        return self.is_element_clickable(self.CART)

    def click_cart_button(self):
        self.click(self.CART)
    def is_become_seller_button_clickable(self):
        return self.is_element_clickable(self.BECOME_SELLER)

    def click_become_seller_button(self):
        self.click(self.BECOME_SELLER)

    def is_drop_down_clickable(self):
        return self.is_element_clickable(self.DROP_DOWN)
    
    def click_drop_down_button(self):
        self.click(self.DROP_DOWN)

    def hover_over_drop_down(self):
        self.hover_over_element(self.DROP_DOWN)

    def is_hovering_over_drop_down_displaying_help_links(self):
        return self.is_element_visible(self.NOTIFICATION_PREFERENCES)

    def is_notification_preference_link_clickable(self):
        return self.is_element_clickable(self.NOTIFICATION_PREFERENCES)
    def is_customer_care_link_clickable(self):
        return self.is_element_clickable(self.CUSTOMER_CARE)
    def is_advertise_link_clickable(self):
        return self.is_element_clickable(self.ADVERTISE)
    def is_download_app_link_clickable(self):
        return self.is_element_clickable(self.DOWNLOAD_APP)
    def click_notification_preference(self):
        self.click(self.NOTIFICATION_PREFERENCES)
    def click_customer_care(self):
        self.click(self.CUSTOMER_CARE)
    def click_advertise(self):
        self.click(self.ADVERTISE)
    def click_download_app(self):
        self.click(self.DOWNLOAD_APP)
    
    # ==================== CATEGORY NAVIGATION ====================

    def is_category_element_visible(self,locator):
        return self.is_element_clickable(locator)

    # ==================== hover over an element ====================

    def hover_over_fashion(self):
        self.hover_over_element(self.FASHION_LINK)
    def hover_over_electronics(self):
        self.hover_over_element(self.ELECTRONICS_LINK)
    def hover_over_home(self):
        self.hover_over_element(self.HOME_FURNITURE_LINK)
    def hover_over_beauty_toys(self):
        self.hover_over_element(self.BEAUTY_LINK)

    # ==================== CATEGORY CLICK METHODS ====================
    def click_minutes(self):
        self.click(self.MINUTES_LINK)

    def click_mobiles_tablets(self):
        self.click(self.MOBILES_TABLETS_LINK)

    def click_tvs_appliances(self):
        self.click(self.TVS_APPLIANCES_LINK)

    def click_flight_bookings(self):
        self.click(self.FLIGHT_BOOKINGS_LINK)

    def click_grocery(self):
        self.click(self.GROCERY_LINK)


    #===================== search box methods =============================================
    def enter_text_into_search(self,text):
         self.enter_text(self.SEARCH_BAR,text)

    def click_search(self):
        self.click(self.SEARCH_BUTTON)

    def search_error_message(self):
        return self.get_text(self.SEARCH_ERROR)