from selenium_lessons.pages.main_page import MainPage


def test_guest_should_see_login_link(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209?promo=midsummer"
    page = MainPage(browser_chrome, link)
    page.open()
    page.should_be_login_link()
