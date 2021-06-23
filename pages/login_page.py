from pages.base_page import BasePage

from pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
    # вызов методов проверки 

        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

# проверяем наличие ссылки на страницу логина

    def should_be_login_url(self):
        assert "/login" in self.browser.current_url, "Login not presented in current URL"

# проверяем наличие элемента с формой для входа в аккаунт

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"
        
# проверяем наличие элемента с формой для регистрации клиента

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"
        