import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math

@pytest.mark.lesson2
def test_lesson2_6_step8(browser_chrome):
    browser = browser_chrome
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    book_button = browser.find_element(By.XPATH, "//button[@id='book']")

    price = WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100"))
    book_button.click()

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    y = calc(x_value)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(7)
