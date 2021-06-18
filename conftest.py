import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", # добавляем возможность выбора браузера для запуска теста, по умолчанию выбран Chrome
                        help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en", help="Choose language: ru or en") # добавляем возможность выбора языка для запуска теста, по умолчанию не выбран ни один



@pytest.fixture(scope="function") # задание фикстуры
def browser(request): 
    browser_name = request.config.getoption("browser_name") # переменная считывает какой браузер выбран
    user_language = request.config.getoption("language") # переменная считывает какой язык выбран
    if (browser_name == "chrome"): # если выбран браузер Chrome
        options = Options() 
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language}) # передача данных о языке в запрос к браузеру 
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options) # открывает браузер Chrome

    elif (browser_name == "firefox"): # если выбран браузер Firefox
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language) # передача данных о языке в запрос к браузеру
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp) # открывает браузер Firefox
    else:
        print("Browser <browser_name> still is not implemented") # выводить сообщение если браузер не выбран
        raise pytest.UsageError("--browser_name should be chrome or firefox") # текст сообщения об ошибке
    yield browser
    print("\nquit browser..")
    browser.quit() # закрытие браузера