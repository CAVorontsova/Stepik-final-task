
from pages.locators import BasePageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage():
    #def __init__(self, browser, url): # создаем конструктор. В качестве параметров мы передаем экземпляр драйвера и url адрес
        #self.browser = browser
        #self.url = url

    def open(self):                  # метод для открытия страницы в браузере
        self.browser.get(self.url)

    def __init__(self, browser, url, timeout=10): # создаем конструктор. В качестве параметров мы передаем экземпляр драйвера и url адрес
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def is_element_present(self, how, what):  # метод для проверки присутствия элемента на странице
        try:
            self.browser.find_element(how,what)
        except (NoSuchElementException):
            return False
        return True


    def go_to_login_page(self):               # метод для перехода на страницу логина
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):          # метод для проверки наличия ссылки на страницу логина
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

# метод, который проверяет, что элемент не появляется на странице в течение заданного времени.
# Если элемент все таки появляется или сразу есть, то тест падает

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

# метод, который проверяет что, какой-то элемент исчезает
#, то следует воспользоваться явным ожиданием вместе с функцией until_not, в зависимости от того, какой результат мы ожидаем
    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
            until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False
        return True


    def go_to_basket (self):                    # метод для перехода в корзину по кнопке из Header
        look_in_basket = self.browser.find_element(*BasePageLocators.LOOK_IN_BASKET)
        look_in_basket.click()




    
