import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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
