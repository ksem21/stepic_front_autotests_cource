import pytest

from selenium_lessons.pages.locators import ProductPageLocators
from selenium_lessons.pages.product_page import ProductPage


@pytest.mark.xfail
def test_lesson4_3_6_1(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser_chrome, link)
    product_page.open()
    product_page.add_to_cart()
    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение присутствует"


def test_lesson4_3_6_2(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser_chrome, link)
    product_page.open()
    assert product_page.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение присутствует"


@pytest.mark.xfail
def test_lesson4_3_6_3(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    product_page = ProductPage(browser_chrome, link)
    product_page.open()
    product_page.add_to_cart()
    assert product_page.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Сообщение присутствует"
