from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import math


def test_lesson2_1_step5(browser):
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser.implicitly_wait(5)

    browser.get("https://suninjuly.github.io/math.html")
    selector_value = browser.find_element(By.XPATH, "//span[@class='nowrap'][@id='input_value']")
    print('Значение селектора', selector_value)
    x = selector_value.text
    print('Значение x', x)

    y = calc(x)

    input_area = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_area.send_keys(y)

    checkbox_area = browser.find_element(By.XPATH, "//input[@class='form-check-input'][@type='checkbox']")
    checkbox_area.click()

    radioinput_area = browser.find_element(By.XPATH, "//input[@class='form-check-input'][@id='robotsRule']")
    radioinput_area.click()

    enter_button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    enter_button.click()
    time.sleep(7)
