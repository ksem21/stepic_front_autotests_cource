from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        need_url = "login"
        assert need_url in current_url, f"ОР: url содержит '{need_url}', ФР: url такой - '{current_url}'"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Нет формы авторизации"
        # реализуйте проверку, что есть форма логин

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Нет формы регистрации"
        # реализуйте проверку, что есть форма регистрации на странице
