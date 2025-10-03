from selenium_lessons.pages.product_page import ProductPage


def test_lesson4_3_2(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    product_page = ProductPage(browser_chrome, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.solve_quiz_and_get_code()
    product_page.check_name_product()
    product_page.check_sum_cart()
