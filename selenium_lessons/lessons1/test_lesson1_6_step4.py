from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest

@pytest.mark.lesson1
def test_lesson1_1_step4(browser_chrome):
    link = "http://suninjuly.github.io/simple_form_find_task.html"

    try:
        browser = browser_chrome
        browser.get(link)

        input1 = browser.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = browser.find_element(By.CLASS_NAME, "city")
        input3.send_keys("Smolensk")
        input4 = browser.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(7)
        # закрываем браузер после всех манипуляций
