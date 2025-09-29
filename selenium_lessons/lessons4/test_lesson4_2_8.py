from selenium_lessons.pages.login_page import LoginPage
from selenium_lessons.pages.main_page import MainPage
from selenium_lessons.pages.locators import LoginPageLocators


def test_test_lesson4_2_8(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = MainPage(browser_chrome, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser_chrome, link)
    login_page.should_be_login_url()
    login_page.should_be_login_form(*LoginPageLocators.LOGIN_FORM), "Нет формы авторизации"
    login_page.should_be_register_form(*LoginPageLocators.REGISTRATION_FORM), "Нет формы регистрации"
