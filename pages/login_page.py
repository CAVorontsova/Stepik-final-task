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

# регистрируем нового пользователя

    def register_new_user(self,email,password):
        input1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_EMAIL)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD)
        input2.send_keys(password)
        input3 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_PASSWORD2)
        input3.send_keys(password)
        button1 = self.browser.find_element(*LoginPageLocators.REGISTER_FORM_BUTTON)
        button1.click()

        