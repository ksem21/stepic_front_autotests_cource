from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_lesson2_2_step3():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("http://suninjuly.github.io/selects1.html")

    first_value = int(browser.find_element(By.XPATH, "//span[@id='num1']").text)
    second_value = int(browser.find_element(By.XPATH, "//span[@id='num2']").text)

    result = first_value + second_value

    browser.find_element(By.XPATH, "//select[@class='custom-select']").click()
    browser.find_element(By.XPATH, f"//option[@value='{result}']").click()
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(7)
    browser.quit()
