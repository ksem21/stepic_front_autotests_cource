from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest


@pytest.mark.lesson2
def test_lesson2_3_step6(browser):
    browser.implicitly_wait(5)

    browser.get("https://suninjuly.github.io/redirect_accept.html")
    browser.find_element(By.XPATH, "//button[@type='submit']").click()

    first_window = browser.window_handles[0]
    second_window = browser.window_handles[1]

    browser.switch_to.window(second_window)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    y = calc(x_value)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(3)
