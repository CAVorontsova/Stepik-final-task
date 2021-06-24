import time
import pytest
from faker import Faker
from pages.basket_page import BasketPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage

# фиктура для проверки нескольких страниц с промо-кодами
#@pytest.mark.parametrize('promo_offer', ["0", "1", "2", "3", "4", "5", "6", pytest.param("7", marks=pytest.mark.xfail), "8", "9"])


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self,browser): # setup-фикстура для регистрации нового пользователя
        link = "https://selenium1py.pythonanywhere.com/accounts/login/"
        self.login_page = LoginPage(browser, link) 
        self.login_page.open() # открываем страницу логина
        f = Faker()
        email = f.email() # генерируем фейковый email
        password = "aB_D1F-Hi" # задаем пароль

        self.login_page.register_new_user(email, password) # регистрируем нового пользователя 
        self.login_page.should_be_authorized_user() # проверяем что пользователь авторизован

# проверяем, что пользователь не видит сообщение о добавлении товара в пустой корзине

    def test_user_cant_see_success_message(self,browser): 
        link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
        self.product_page = ProductPage(browser,link)
        self.product_page.open()
        self.product_page.cant_see_success_message()

# проверяем, что пользователь может добавить товар в корзину
    @pytest.mark.need_review
    def test_user_can_add_product_to_basket (self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_208"
        self.add_to_basket = ProductPage(browser,link)
        self.add_to_basket.open()
        self.add_to_basket.add_to_basket()
        self.add_to_basket.compare_product_name()
        self.add_to_basket.compare_product_price()

# тест проверяет, что название и цена товара в корзине, соответствует выбранным пользователем

@pytest.mark.parametrize('promo_offer', ["0"])
def test_guest_can_add_product_to_basket (browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.compare_product_name()
    page.compare_product_price()

# тест проверяет, что после добавления товара в корзину не появляется сообщение об успешном добавлении
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.cant_see_success_message()

# тест проверяет, что после открытия страницы с товаром не появляется сообщение об успешном добавлении товара в корзину

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    page = ProductPage(browser,link)
    page.open()
    page.cant_see_success_message()

# тест, который проверяет пропадает ли сообщение об успешном добавлении товара в корзину через какое-то время

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207"
    page = ProductPage(browser,link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.success_message_is_disapeared()

# тест проверяет, что пользователь на странице продукта видит ссылку на страницу логина

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

# тест проверяет, что пользователь может перейти со страницы продукта на страницу логина
@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

# тест проверяет, что пользователь не видит товаров в пустой корзине
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.no_books_in_basket()
    basket_page.empty_basket_message()
    time.sleep(5)









    

