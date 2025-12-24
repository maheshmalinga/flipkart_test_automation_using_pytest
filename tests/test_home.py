import pytest
from pages.home_page import HomePage

@pytest.fixture
def home_class(driver1):
    home = HomePage(driver1)
    home.open_homepage()
    yield home

@pytest.fixture
def home(driver):
    home = HomePage(driver)
    home.open_homepage()
    try:
        home.close_pop_up()
    finally:
        return home

@pytest.mark.smoke
class TestHomePageHeader:

    def test_is_home_page_loaded_successfully(self,home_class):
        assert home_class.is_homepage_loaded()

    def test_logo_button(self,home_class):
        try:
            home_class.close_pop_up()
        finally:
            home_class.click_logo()
        assert home_class.is_homepage_loaded()

    def test_is_login_button_clickable(self,home_class):
        assert home_class.is_login_button_clickable()

    def test_is_cart_button_clickable(self,home_class):
        assert home_class.is_cart_button_visible_and_clickable()

    def test_is_drop_down_button_clickable(self,home_class):
        assert home_class.is_drop_down_visible_and_clickable()

@pytest.mark.regression
class TestCategoryLinks:
    def test_minutes_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.MINUTES_LINK)

    def test_mobiles_tablets_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.MOBILES_TABLETS_LINK)

    def test_tvs_appliaces_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.TVS_APPLIANCES_LINK)

    def test_electronics_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.ELECTRONICS_LINK)

    def test_fashion_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.FASHION_LINK)

    def test_home_kitchen_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.HOME_KITCHEN_LINK)

    def test_beauty_toys_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.BEAUTY_TOYS_LINK)

    # def test_furniture_link_displayed(self,home_class):
    #     assert home_class.is_category_element_visible(home_class.FURNITURE_LINK)

    def test_flight_bookings_link_displayed(self, home_class):
        assert home_class.is_category_element_visible(home_class.FLIGHT_BOOKINGS_LINK)

    def test_grocery_link_displayed(self, home_class):
        assert home_class.is_category_element_visible(home_class.GROCERY_LINK)
@pytest.mark.regression
class TestCategoryNavigation:
    """test cases for category navigation"""
    def test_click_minutes_link(self,home,driver):
        home.click_minutes()
        assert home.url != driver.current_url
    def test_clik_mobiles_tablets(self,home,driver):
        home.click_mobiles_tablets()
        assert "mobile" in driver.current_url
    def test_click_tvs_appliances(self,home,driver):
        home.click_tvs_appliances()
        assert "tvs" in  driver.current_url or "appliances" in driver.current_url
    # def test_click_electronics(self,home,driver):
    #     home.click_electronics()
    #     assert home.url != driver.current_url
    # def test_click_fashion(self, home, driver):
    #     home.click_fashion()
    #     assert home.url != driver.current_url
    # def test_click_home_kitchen(self, home, driver):
    #     home.click_home_kitchen()
    #     assert home.url != driver.current_url
    # def test_click_beauty_toys(self,home,driver):
    #     home.click_beauty_toys()
    #     assert home.url != driver.current_url
    # def test_click_furniture(self,home,driver):
    #     home.click_furniture()
    #     assert "furniture" in driver.current_url or driver.title == "Winter Bonanza Store Online - Buy Winter Bonanza Online at Best Price in India | Flipkart.com"
    def test_click_flight_bookings(self,driver,home):
        home.click_flight_bookings()
        assert "flight" in driver.current_url
    def test_click_grocery(self,home,driver):
        home.click_grocery()
        assert "grocery" in driver.current_url
@pytest.mark.smoke
class TestSearchFunctionality:
    def test_search_with_valid_product(self,home,driver):
        home.enter_text_into_search("mi phone 14 ")
        home.click_search()
        assert "mi" in driver.current_url
    def test_search_with_special_character(self,home,driver):
        home.enter_text_into_search("@")
        home.click_search()
        assert home.search_error_message() in "Sorry, no results found!"
    def test_search_with_empty_query(self,home,driver):
        home.enter_text_into_search("")
        home.click_search()
        assert driver.current_url == home.url
