from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


def test_lesson2_2_step8():
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)

    browser.get("https://suninjuly.github.io/file_input.html")
    browser.find_element(By.XPATH, "//input[@name='firstname']").send_keys("Dmitry")
    browser.find_element(By.XPATH, "//input[@name='lastname']").send_keys("Kazadanov")
    browser.find_element(By.XPATH, "//input[@name='email']").send_keys("kds@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого
    file_path = os.path.join(current_dir, 'lesson2_2_step8.txt')  # добавляем к этому пути имя файла

    browser.find_element(By.XPATH, "//input[@type='file']").send_keys(file_path)
    browser.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(7)
    browser.quit()
