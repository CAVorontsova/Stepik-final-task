
import time

link = "http://selenium1py.pythonanywhere.com/"

def go_to_login_page(browser):
    login_link = browser.find_element_by_css_selector("#login_link")
    login_link.click()

# поиск кнопки для логина и перехода на страницу логина вынесен в отдельное действие
# поскольку функция go_to_login_page не начинается с test, то python ее пропустит и она не будет выполняться первой.
# Вызов идет из функции test_guest_can_go_to_login_page 

def test_guest_can_go_to_login_page(browser):
    browser.get(link)
    go_to_login_page(browser)
    time.sleep(5)