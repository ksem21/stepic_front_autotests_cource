from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import pytest


@pytest.mark.lesson2
def test_lesson2_1_step7(browser_chrome):
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    browser = browser_chrome
    browser.implicitly_wait(5)

    browser.get("https://suninjuly.github.io/get_attribute.html")

    treasure_img = browser.find_element(By.XPATH, "//img[@id='treasure']")
    value_treasure_img = treasure_img.get_attribute("valuex")
    y = calc(value_treasure_img)

    input_area = browser.find_element(By.XPATH, "//input[@id='answer']")
    input_area.send_keys(y)

    checkbox_area = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    checkbox_area.click()

    radioinput_area = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    radioinput_area.click()

    enter_button = browser.find_element(By.XPATH, "//button[@class='btn btn-default']")
    enter_button.click()
    time.sleep(7)
