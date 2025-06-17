from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
driver = webdriver.Chrome()

try:

    driver.get(link)
    first_name = driver.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input")
    first_name.send_keys("Ivan")
    last_name = driver.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input")
    last_name.send_keys("Ivanov")
    email = driver.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
    email.send_keys("ivan.ivanov@gmail.ru")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(5)
    driver.quit()