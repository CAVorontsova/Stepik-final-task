from selenium.webdriver.common.by import By

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # элемент с ссылкой на страницу логина


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # элемент с формой для входа в аккаунт
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # элемент с формой для регистрации

class ProductPageLocators():
    BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket") # кнопка добавления товара в корзину
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.col-sm-6.product_main h1") # название книги, выбранной пользователем
    BOOK_IN_BASKET_NAME = (By.CSS_SELECTOR, "div.alertinner strong") # название книги в корзине
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.col-sm-6.product_main .price_color") # цена товара, выбранного пользователем
    BOOK_IN_BASKET_PRICE = (By.CSS_SELECTOR, "div.alertinner p strong") # цена товара в корзине
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alert-success") # элемент с сообщением о добавлении товара в корзину

# класс для проверки ссылки на страницу логина

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")