import os

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import math
from dotenv import load_dotenv

load_dotenv()
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1:
    links = ['https://stepik.org/lesson/236895/step/1',
             'https://stepik.org/lesson/236896/step/1',
             'https://stepik.org/lesson/236897/step/1',
             'https://stepik.org/lesson/236898/step/1',
             'https://stepik.org/lesson/236899/step/1',
             'https://stepik.org/lesson/236903/step/1',
             'https://stepik.org/lesson/236904/step/1',
             'https://stepik.org/lesson/236905/step/1']
    answer = ''
    @pytest.mark.parametrize('link', links)
    def test_stepik_page(self, browser, link):
        browser.get(link)
        login_link = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a.navbar__auth_login'))
        )
        browser.execute_script("arguments[0].click();", login_link)

        form = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.ID, "login_form"))
        )
        input_login = form.find_element(By.NAME, 'login')
        input_login.send_keys(os.getenv('LOGIN'))
        input_password = form.find_element(By.NAME, 'password')
        input_password.send_keys(os.getenv('PASSWORD'))
        button = form.find_element(By.CSS_SELECTOR, "button")
        button.click()

        time.sleep(2)

        answer_place = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'div.attempt'))
        )
        textarea = WebDriverWait(answer_place, 15).until(
            EC.element_to_be_clickable((By.TAG_NAME, 'textarea'))
        )
        textarea.send_keys(str(math.log(int(time.time()))))
        button = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.submit-submission'))
        )
        button.click()

        value = WebDriverWait(browser, 15).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.attempt__message p'))
        )
        assert value.text == 'Correct!', f'Url {link} with not correct answer {value.text}'
