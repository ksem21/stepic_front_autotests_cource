import pytest

import personal_info

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.mark.lesson3
@pytest.mark.parametrize('link', ["https://stepik.org/lesson/236895/step/1", "https://stepik.org/lesson/236896/step/1",
                                  "https://stepik.org/lesson/236897/step/1", "https://stepik.org/lesson/236898/step/1",
                                  "https://stepik.org/lesson/236899/step/1", "https://stepik.org/lesson/236903/step/1",
                                  "https://stepik.org/lesson/236904/step/1",
                                  "https://stepik.org/lesson/236905/step/1"])
def test_lessom3_6_step4(browser, link):
    browser.get(link)
    browser.implicitly_wait(5)

    # 1. Находим кнопку авторизации и нажимаем
    auth_button = browser.find_element(By.XPATH,
                                       "//a[@class='ember-view navbar__auth navbar__auth_login st-link st-link_style_button']")
    auth_button.click()

    # 2. Находим поле логина и вводим данные
    email_field = browser.find_element(By.XPATH, "//input[@name='login']")
    email_field.send_keys(personal_info.stepic_login)

    # 3. Находим поле пароля и вводим данные
    password_field = browser.find_element(By.XPATH, "//input[@name='password']")
    password_field.send_keys(personal_info.stepic_password)

    # 4. Находим кнопку подтверждения и нажимаем
    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    # 5. Находим кнопку, которая показывает, что мы авторизованы
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//img[@class='navbar__profile-img']")))

    # 6. Считаем ответ
    answer = math.log(int(time.time()))
    # 7. Находим поле ввода для ответа и вводим данные
    input_area_for_answer = browser.find_element(By.XPATH,
                                                 "//textarea[@class='ember-text-area ember-view textarea string-quiz__textarea']")
    input_area_for_answer.send_keys(answer)

    # 8. Находим кнопку "Отправить" и ждем пока она будет кликабельной
    enter_button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@class='submit-submission']")))
    enter_button.click()

    # 9. Находим поле фидбек и сравниваем его значение
    feedback = WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//p[@class='smart-hints__hint']")))
    assert feedback.text == "Correct!", f"ФР: {feedback.text}, ОР: 'Correct!'"

# Нужно доработать тест так, чтобы после его выполнения проходить и нажимать на кнопку "Решить снова"
