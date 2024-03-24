from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)
    # ожидание появления текста в элементе по локатору
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, 'book').click()
    submit_button = browser.find_element(By.ID, "solve")
    # выполнить скролл до кнопки Submit
    browser.execute_script("arguments[0].scrollIntoView();", submit_button)
    # пример тестовой функции
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)

    # отправляем заполненную форму
    browser.find_element(By.ID, "solve").click()

    # ждем загрузки страницы
    # чтобы было время сохранить результат
    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

