from selenium.webdriver.common.by import By

#class MainPageLocators():
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link") # элемент с ссылкой на страницу логина

# класс для проверки наличия форм для логина и регистрации пользователя

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form") # элемент с формой для входа в аккаунт
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") # элемент с формой для регистрации

# класс для проверки добавления товара в корзину

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
    LOOK_IN_BASKET = (By.CSS_SELECTOR, "span.btn-group a.btn-default")

# класс для проверки пустой корзины

class BasketPageLocators():
    BOOKS_IN_BASKET = (By.CSS_SELECTOR, "div.basket-items")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")