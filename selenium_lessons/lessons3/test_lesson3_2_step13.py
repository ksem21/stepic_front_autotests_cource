from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestAbs(unittest.TestCase):
    def test_lesson3_2_step13(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_name_input.send_keys("Дмитрий")

        last_name_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        last_name_input.send_keys("Казаданов")

        email_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email_input.send_keys("kds@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"ОР: 'Congratulations! You have successfully registered!', ФР: {welcome_text}")

    def test_lesson3_2_step13_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        first_name_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your first name']")
        first_name_input.send_keys("Дмитрий")

        last_name_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
        last_name_input.send_keys("Казаданов")

        email_input = browser.find_element(By.XPATH, "//input[@placeholder='Input your email']")
        email_input.send_keys("kds@mail.ru")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         f"ОР: 'Congratulations! You have successfully registered!', ФР: {welcome_text}")


if __name__ == "__main__":
    unittest.main()
