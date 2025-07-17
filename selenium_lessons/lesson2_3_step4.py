from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get("https://suninjuly.github.io/alert_accept.html")
browser.find_element(By.XPATH, "//button[@type='submit']").click()
alert = browser.switch_to.alert
alert.accept()


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


x_value = browser.find_element(By.XPATH, "//span[@id='input_value']").text
y = calc(x_value)
browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(y)
browser.find_element(By.XPATH, "//button[@type='submit']").click()
time.sleep(7)
