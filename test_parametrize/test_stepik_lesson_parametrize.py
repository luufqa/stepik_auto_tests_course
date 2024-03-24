from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from config import User
import pytest
import math
import time


class TestParametrize:

    @pytest.mark.parametrize("links", ["https://stepik.org/lesson/236895/step/1",
                                       "https://stepik.org/lesson/236896/step/1",
                                       "https://stepik.org/lesson/236897/step/1",
                                       "https://stepik.org/lesson/236898/step/1",
                                       "https://stepik.org/lesson/236899/step/1",
                                       "https://stepik.org/lesson/236903/step/1",
                                       "https://stepik.org/lesson/236904/step/1",
                                       "https://stepik.org/lesson/236905/step/1"])
    def test_parametrize(self, browser, links):
        # так как ресурс, к которому обращаемся нестабилен
        # приходится импровизировать
        """Во всех упавших тестах можно найти ответ на задание"""
        try:
            browser.get(links)
            WebDriverWait(browser, 15).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, '.ember-view.navbar__auth.navbar__auth_login.st-link.st-link_style_button'))).click()
            browser.find_element(By.ID, 'id_login_email').send_keys(User.login)
            browser.find_element(By.ID, 'id_login_password').send_keys(User.password)
            browser.find_element(By.CSS_SELECTOR, '.sign-form__btn.button_with-loader').click()
            time.sleep(15)
            sl = browser.find_element(By.CSS_SELECTOR, 'button.again-btn')
            ActionChains(browser).move_to_element(sl).click().perform()
            time.sleep(10)
            sd = browser.find_element(By.XPATH, '/html/body/div[5]/div/div/footer/button[1]')
            ActionChains(browser).move_to_element(sd).click().perform()
            time.sleep(10)
        except NoSuchElementException:
            browser.find_element(By.CSS_SELECTOR, 'div.quiz-component.ember-view > textarea').clear()
            number = math.log(int(time.time()))
            browser.find_element(By.CSS_SELECTOR, '.ember-text-area').send_keys(number)
            browser.find_element(By.CSS_SELECTOR, '.submit-submission').click()
            time.sleep(1)
            answer = browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text
            time.sleep(1)
            assert 'Correct!' in answer, f"{answer}"
