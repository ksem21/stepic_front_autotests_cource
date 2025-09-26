from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest


@pytest.mark.lesson2
def test_lesson2_2_step6(browser_chrome):
    browser = browser_chrome
    browser.implicitly_wait(5)

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    link = "https://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
    y = calc(x_value)

    # Скролл страницы на 115px
    browser.execute_script("window.scrollBy(0, 115);")

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
    browser.find_element(By.XPATH, "//input[@id='robotCheckbox']").click()
    browser.find_element(By.XPATH, "//input[@id='robotsRule']").click()
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(7)
