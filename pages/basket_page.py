from pages.locators import BasketPageLocators
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

    
class BasketPage(BasePage):
    def no_books_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BOOKS_IN_BASKET), \
        "Books in the basket is presented, but should not be"
    def empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
        "Basket not empty, but should be" 
    