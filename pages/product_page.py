from pages.base_page import BasePage
from pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoAlertPresentException
import math

class ProductPage(BasePage):
# нажимаем на кнопку положить в корзину
    def add_to_basket (self):
        basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
        basket_button.click()

# решаем математическое выражение и получаем код. Выводим его в консоль

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

# сравниваем название книги на странице и название книги в корзине
    

    def compare_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        book_in_basket_name = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET_NAME).text
        assert book_in_basket_name == product_name , "There is another book in the basket"

# сравниваем стоимость книги на странице и стоимость книги в корзине

    def compare_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        book_in_basket_price = self.browser.find_element(*ProductPageLocators.BOOK_IN_BASKET_PRICE).text
        assert book_in_basket_price == product_price, "There is another book price"