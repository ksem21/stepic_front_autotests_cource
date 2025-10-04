from selenium_lessons.pages.product_page import ProductPage


def test_lesson4_3_8_1(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser_chrome, link)
    page.open()
    page.should_be_login_link()


def test_lesson4_3_8_2(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser_chrome, link)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()
