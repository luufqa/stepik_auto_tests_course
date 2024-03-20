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
    # Ожидание появления текста в элементе по локатору
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, 'book').click()
    submit_button = browser.find_element(By.ID, "solve")
    # Выполнить скролл до кнопки Submit
    browser.execute_script("arguments[0].scrollIntoView();", submit_button)
    # Пример тестовой функции
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))

    x = browser.find_element(By.ID, 'input_value').text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)

    # Отправляем заполненную форму
    browser.find_element(By.ID, "solve").click()

    # ждем загрузки страницы
    # и чтобы было время сохранить результат
    time.sleep(10)


finally:
    # закрываем браузер после всех манипуляций
    browser.quit()

    # заметки
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    confirm = browser.switch_to.alert
    confirm.accept()
    browser.find_element(By.CSS_SELECTOR, 'input[placeholder="Enter first name"]').send_keys('Alex')
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')
    download_button = browser.find_element(By.ID, "file") # добавляем к этому пути имя файла
    download_button.send_keys(file_path)

    # Прокрутки страницы так, чтобы элемент, на который она применяется был видимым на экране
    browser.execute_script("return arguments[0].scrollIntoView(true);", element)
    # Поиск по значению CSS_SELECTOR
    browser.find_element(By.CSS_SELECTOR, '[value="robots"]').click()
