import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_lessons.pages.login_page import LoginPage
import time


@pytest.fixture()
def browser_chrome():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture()
def browser_for_lesson3_6_step4():
    browser = webdriver.Chrome()
    yield browser

    try:
        try_again = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='again-btn white']")))
        try_again.click()
    except NoSuchElementException:
        # если кнопка не найдена, тест всё равно завершится корректно
        pass
    finally:
        browser.quit()


@pytest.fixture()
def register_user(browser_chrome):
    link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    page = LoginPage(browser_chrome, link)
    page.open()
    email = str(time.time()) + "@fakemail.org"
    password = "pisun123456"
    page.register_new_user(email, password)
    return browser_chrome
