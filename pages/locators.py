from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1")
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, "div.alertinner strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color")
    BOOK_IN_BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong")