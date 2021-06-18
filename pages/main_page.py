from pages.base_page import BasePage  # в исходном варианте кода урока это выражение выглядело так from .base_page import BasePage
# однако у меня вылезала ошибка если я прописывала точку. Согласно комментарию преподавателя такое возможно из-за 
# разницы пакетов. Это не критично
# Импорт для разных случаев записывается так /корень текущего диска - без точки
                                          # ./текущая директория
                                          # ../родитель текущей директории
# поскольку будем обращаться к этому файлу из test_main_page.py то пришлось добавить еще и pages перед base_page


from selenium.webdriver.common.by import By

from pages.locators import MainPageLocators

from pages.login_page import LoginPage

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()


# Файлы base_page и main_page были сделаны чтобы разделить тесты и методы
# и чтобы у нас была возможность использовать один метод в нескольких тестах не переписывая его
# base_page это как бы реализация общих методов для любой странички.
# Дальше идет реализация методов конкретных страниц, например: main_page, login_page, basket_page
# А в файлах типа test_main_page, test_login_page - сами тесты


    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"