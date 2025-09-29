from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException

class LoginPage(BasePage):
    # def should_be_login_page(self):
    #     self.should_be_login_url()
    #     self.should_be_login_form()
    #     self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        need_url = "login"
        assert need_url in current_url, f"ОР: {need_url}, ФР: {current_url}"
        # реализуйте проверку на корректный url адрес

    def should_be_login_form(self, how, what):
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
        # реализуйте проверку, что есть форма логин

    def should_be_register_form(self, how, what):
        # реализуйте проверку, что есть форма регистрации на странице
        try:
            self.browser.find_element(how, what)
        except(NoSuchElementException):
            return False
        return True
