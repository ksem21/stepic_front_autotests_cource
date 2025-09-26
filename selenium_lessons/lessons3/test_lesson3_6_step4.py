import pytest

import personal_info

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.lesson3
def test_lessom3_6_step4(browser_chrome):
    browser = browser_chrome
    browser.get("https://stepik.org/lesson/236895/step/1")
    browser.implicitly_wait(5)

    auth_button = browser.find_element(By.XPATH, "//a[@id='ember484']")
    auth_button.click()

    modal_window = browser.find_element(By.XPATH, "//div[@class='light-tabs ember-view']")
    assert modal_window.is_displayed(), "Модальное окно не открылось"

    email_field = browser.find_element(By.XPATH, "//input[@name='login']")
    email_field.send_keys(personal_info.stepic_login)

    password_field = browser.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys(personal_info.stepic_password)

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    WebDriverWait(browser, 5).until(
        EC.invisibility_of_element(modal_window)
    )
