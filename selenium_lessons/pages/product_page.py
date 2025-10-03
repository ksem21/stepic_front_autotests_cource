from selenium_lessons.pages.locators import ProductPageLocators
from .base_page import BasePage
import math
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):
    def add_to_cart(self):
        add_btn = self.browser.find_element(
            *ProductPageLocators.ADD_BTN)
        add_btn.click()

    # Код для решения задачи, написанный на степике
    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def check_name_product(self):
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        name_of_product_in_cart = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_CART).text
        assert name_of_product == name_of_product_in_cart, f"ОР: Добавлен товар '{name_of_product}', ФР: Добавлен товар '{name_of_product_in_cart}'"

    def check_sum_cart(self):
        cost_of_product = self.browser.find_element(*ProductPageLocators.COST_OF_PRODUCT).text
        total_cost_of_cart = self.browser.find_element(*ProductPageLocators.TOTAL_COST_OF_CART).text
        assert cost_of_product == total_cost_of_cart, f"ОР: Стоимость корзины '{cost_of_product}', ФР: Стоимость корзины '{total_cost_of_cart}'"
