from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    #first_block
    first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input")
    first_name.send_keys("Ivan")
    last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input")
    last_name.send_keys("Ivanovich")
    email_input = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input")
    email_input.send_keys("test@gmail.com")

    #second_block
    first_name = browser.find_element(By.CSS_SELECTOR, "div.second_block div.first_class input")
    first_name.send_keys("98797")
    last_name = browser.find_element(By.CSS_SELECTOR, "div.second_block div.second_class input")
    last_name.send_keys("asdf")

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
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()