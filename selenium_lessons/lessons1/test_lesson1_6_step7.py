from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_lesson1_1_step7():
    try:
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/huge_form.html")
        elements = browser.find_elements(By.CSS_SELECTOR, "input")
        for element in elements:
            element.send_keys("Мой ответ")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        # успеваем скопировать код за 30 секунд
        time.sleep(7)
        # закрываем браузер после всех манипуляций
    browser.quit()
