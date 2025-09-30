from selenium_lessons.pages.login_page import LoginPage
from selenium_lessons.pages.main_page import MainPage


def test_test_lesson4_2_8(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=midsummer"
    page = MainPage(browser_chrome, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser_chrome, browser_chrome.current_url)
    login_page.should_be_login_page()
