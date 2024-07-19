from pages.base_page import BasePage
from pages.index_page import IndexPage
from pages.index_page_locators import IndexPageLocators
from resources.constants import MAX_WAIT_INTERVAL, TEST_SITE_URL, SIGN_ON_BTN_TEXT
from pages.flight_finder_page_locators import FlightFinderPageLocators


# index page
class FlightFinderPage(BasePage):
    def flight_finder_check(self):
        self.driver.refresh()
        index_page = IndexPage(self.driver)
        index_page.go_to_flight_reservation()
        flight_finder_text = self.find_element(FlightFinderPageLocators.FLIGHT_FINDER_LBL).text
        if flight_finder_text == "Flight Details":
            return True
        else:
            return False
