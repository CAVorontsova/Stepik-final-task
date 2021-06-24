import pytest
import time
from pages.base_page import BasePage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage



# поиск кнопки для логина и перехода на страницу логина вынесен в отдельное действие
# поскольку функция go_to_login_page не начинается с test, то python ее пропустит и она не будет выполняться первой.
# Вызов идет из функции test_guest_can_go_to_login_page 

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasePage(browser, link)   # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                      # открываем страницу
    page.go_to_login_page() # выполняем метод страницы — переходим на страницу логина
    time.sleep(5)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()
    



def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/" 
    page = BasePage(browser, link) # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес 
    page.open()                    # открываем страницу
    page.should_be_login_link()    # выполняем метод страницы — проверяем наличие ссылки на сраницу логина


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "https://selenium1py.pythonanywhere.com/ru/catalogue/"
    page = BasePage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.no_books_in_basket()
    basket_page.empty_basket_message()
    time.sleep(5)

















    