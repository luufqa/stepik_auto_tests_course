from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import unittest


class TestLesson(unittest.TestCase):
    def test_registration1(self):
        try:
            # ссылка на старую форму регистрации, где все работает
            link = "http://suninjuly.github.io/registration1.html"
            browser = webdriver.Firefox()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys('alex1')
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys('alex2')
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys('alex3')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.container > h1")))
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            # закрываем браузер
            browser.quit()

    def test_registration2(self):
        try:
            # ссылка на новую форму регистрации (после обновления), где тест не проходит
            link = "http://suninjuly.github.io/registration2.html"
            browser = webdriver.Firefox()
            browser.get(link)

            # Ваш код, который заполняет обязательные поля
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your first name"]').send_keys('alex1')
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your last name"]').send_keys('alex2')
            browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Input your email"]').send_keys('alex3')

            # Отправляем заполненную форму
            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            # Проверяем, что смогли зарегистрироваться
            # ждем загрузки страницы
            WebDriverWait(browser, 12).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.container > h1")))
            # находим элемент, содержащий текст
            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            # записываем в переменную welcome_text текст из элемента welcome_text_elt
            welcome_text = welcome_text_elt.text

            # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
            assert "Congratulations! You have successfully registered!" == welcome_text
        finally:
            # закрываем браузер
            browser.quit()


if __name__ == "__main__": unittest.main()

# чтобы получить решения по уроку - необходимо выполнить команду
# python3 test_stepik_lesson_unittest.py
# FAILED (errors=1)
