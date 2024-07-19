from pages.login_success_page import LoginSuccessPage
from test_utils import *
from pages.index_page import IndexPage
from pages.register_page import RegisterPage
from pages.register_success_page import RegisterSuccessPage
from resources.constants import TEST_SITE_URL
from pages.flight_finder_page import FlightFinderPage,FlightFinderPageLocators


class TestFlightBooking:

    # Test Case 1 ( Registering the user)
    def test_find_a_flight(self, driver, username_password):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)

        index_page.go_to_flight_reservation()
        flight_finder_page=FlightFinderPage(driver)

        assert flight_finder_page.flight_finder_check(), "Page not Loaded"





