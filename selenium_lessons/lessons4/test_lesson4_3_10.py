from selenium_lessons.pages.base_page import BasePage
from selenium_lessons.pages.locators import BasketLocators


def test_lesson4_3_10_1(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/ru/"
    page = BasePage(browser_chrome, link)
    page.open()
    page.go_to_cart()
    page.is_not_element_present(*BasketLocators.BASKET_ITEMS)
    page.is_element_present(*BasketLocators.EMPTY_CART_PHRASE)


def test_lesson4_3_10_2(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/"
    page = BasePage(browser_chrome, link)
    page.open()
    page.go_to_cart()
    page.is_not_element_present(*BasketLocators.BASKET_ITEMS)
    page.is_element_present(*BasketLocators.EMPTY_CART_PHRASE)
