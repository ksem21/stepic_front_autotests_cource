from selenium_lessons.pages.main_page import MainPage


def test_lesson4_2_2(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser_chrome, link)
    page.open()
    page.go_to_login_page()
