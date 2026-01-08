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
    yield home
@pytest.mark.smoke
@pytest.mark.abcd
class TestHomePageHeaderVisibility:
    """test cases for header elements navigation"""
    def test_is_homepage_loaded_successfully(self,home_class):
        assert home_class.is_homepage_loaded()
    def test_is_logo_button_clickable(self,home_class):
        assert home_class.is_logo_button_clickable()
    def test_is_search_bar_clickable(self,home_class):
        assert home_class.is_search_bar_clickable()
    def test_is_search_button_clickable(self,home_class):
        assert home_class.is_search_button_clickable()
    def test_is_login_button_clickable(self,home_class):
        assert home_class.is_login_button_clickable()
    def test_is_cart_button_clickable(self,home_class):
        assert home_class.is_cart_button_clickable()
    def test_is_become_seller_button_clickable(self,home_class):
        assert home_class.is_become_seller_button_clickable()
    def test_is_drop_down_clickable(self,home_class):
        assert home_class.is_drop_down_clickable()
    def test_hover_over_drop_down(self,home_class):
        home_class.hover_over_drop_down()
        assert home_class.is_drop_down_clickable()
class TestLoginDropDown:
    def test_is_login_dropdown_displayed(self,home,driver):
        home.hover_over_login()
        assert home.is_login_drop_down_displayed()
    def test_is_sign_up_button_displayed(self,home,driver):
        home.hover_over_login()
        assert home.is_sign_up_button_clickable()
    def test_is_my_profile_button_displayed(self,home,driver):
        home.hover_over_login()
        assert home.is_my_profile_button_clickable()
    # def test_is_flipkart_plus_button_displayed(self,home,driver):
    #     home.hover_over_login()
    #     assert home.is_flipkart_plus_button_clickable()
    # def test_is_orders_button_displayed(self,home,driver):
    #     home.hover_over_login()
    #     assert home.is_orders_button_clickable()
    def test_is_wish_list_button_displayed(self,home,driver):
        home.hover_over_login()
        assert home.is_wish_list_button_clickable()


@pytest.mark.smoke
class TestDropDown:
    def test_is_notification_link_displayed(self,home,driver):
        home.hover_over_drop_down()
        assert home.is_notification_preference_link_clickable()
    def test_is_customer_care_link_displayed(self,home,driver):
        home.hover_over_drop_down()
        assert home.is_customer_care_link_clickable()
    def test_is_advertise_link_displayed(self,home,driver):
        home.hover_over_drop_down()
        assert home.is_advertise_link_clickable()
    def test_is_download_link_displayed(self,home,driver):
        home.hover_over_drop_down()
        assert home.is_download_app_link_clickable()
    def test_click_notification_preferences(self,home,driver):
        home.hover_over_drop_down()
        home.click_notification_preference()
        assert "communication" in driver.current_url
    def test_click_customer_care(self,home,driver):
        home.hover_over_drop_down()
        home.click_customer_care()
        assert "helpcentre" in driver.current_url

    def test_click_advertise(self,home,driver):
        home.hover_over_drop_down()
        home.click_advertise()
        assert "advertise" in driver.current_url
    def test_click_download_app(self,home,driver):
        home.hover_over_drop_down()
        home.click_download_app()
        assert "mobile-apps" in driver.current_url


@pytest.mark.integration
class TestHomePageHeader:
    """test cases for header elements navigation"""
    def test_click_logo_button(self,home):
        home.click_logo()
        assert home.is_homepage_loaded()

    def test_search_input(self,home,driver):
        home.enter_text_into_search("abcd")
        home.click_search()
        assert "search" in driver.current_url

    def test_click_login_button(self,home,driver):
        home.click_login_button()
        assert "login" in driver.current_url

    def test_click_cart_button(self,home,driver):
        home.click_cart_button()
        assert "cart" in driver.current_url
    def test_click_become_seller_button(self,home,driver):
        home.click_become_seller_button()
        assert "sell-online" in driver.current_url

    def test_click_drop_down_button(self,home,driver):
        home.click_drop_down_button()
        assert "#" in driver.current_url

@pytest.mark.smoke
@pytest.mark.regression
class TestCategoryLinks:
    """test cases for category visibility"""
    def test_minutes_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.MINUTES_LINK)

    def test_mobiles_tablets_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.MOBILES_TABLETS_LINK)

    def test_tvs_appliances_link_displayed(self, home_class):
        assert home_class.is_category_element_visible(home_class.TVS_APPLIANCES_LINK)

    def test_electronics_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.ELECTRONICS_LINK)

    def test_fashion_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.FASHION_LINK)

    def test_home_kitchen_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.HOME_FURNITURE_LINK)

    def test_beauty_toys_link_displayed(self,home_class):
        assert home_class.is_category_element_visible(home_class.BEAUTY_LINK)

    # def test_furniture_link_displayed(self,home_class):
    #     assert home_class.is_category_element_visible(home_class.FURNITURE_LINK)

    def test_flight_bookings_link_displayed(self, home_class):
        assert home_class.is_category_element_visible(home_class.FLIGHT_BOOKINGS_LINK)

    def test_grocery_link_displayed(self, home_class):
        assert home_class.is_category_element_visible(home_class.GROCERY_LINK)

@pytest.mark.integration
@pytest.mark.regression
class TestCategoryNavigation:
    """test cases for category navigation"""
    def test_click_minutes_link(self,home,driver):
        home.click_minutes()
        assert home.url != driver.current_url
    def test_click_mobiles_tablets(self,home,driver):
        home.click_mobiles_tablets()
        assert "mobile" in driver.current_url
    def test_click_tvs_appliances(self,home,driver):
        home.click_tvs_appliances()
        assert "tvs" in  driver.current_url or "appliances" in driver.current_url
    def test_click_flight_bookings(self,driver,home):
        home.click_flight_bookings()
        assert "flight" in driver.current_url
    def test_click_grocery(self,home,driver):
        home.click_grocery()
        assert "grocery" in driver.current_url
##----------------- hovering the elements ----------------------------------
    def test_hover_over_fashion(self,home,driver):
        home.hover_over_fashion()
        assert home.is_element_clickable(("link text","Men's Top Wear"))
    def test_hover_over_electronics(self,home,driver):
        home.hover_over_electronics()
        assert home.is_element_clickable(("link text","Audio"))
    def test_hover_over_furniture(self,home,driver):
        home.hover_over_home()
        assert home.is_element_clickable(("link text","Home Furnishings"))
    def test_over_beauty_toys(self,home,driver):
        home.hover_over_beauty_toys()
        assert home.is_element_clickable(("link text","Beauty & Personal Care"))
