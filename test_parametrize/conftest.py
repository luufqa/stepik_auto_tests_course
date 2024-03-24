from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\nquit browser..")
    browser.quit()

    from selenium.webdriver.chrome.options import Options

    # options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    # browser = webdriver.Chrome(options=options)
    #
    # fp = webdriver.FirefoxProfile()
    # fp.set_preference("intl.accept_languages", user_language)
    # browser = webdriver.Firefox(firefox_profile=fp)