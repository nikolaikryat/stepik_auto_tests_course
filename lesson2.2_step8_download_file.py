import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import os

link = "https://suninjuly.github.io/file_input.html"
driver = webdriver.Chrome()

try:
    driver.get(link)

    fn = driver.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(2)")
    fn.send_keys("Ivan")

    ln = driver.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(4)")
    ln.send_keys("Ivanov")

    em = driver.find_element(By.CSS_SELECTOR, "body > div > form > div > input:nth-child(6)")
    em.send_keys("Ivanov.Ivan@gmail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, '2.2_step8.txt')
    element = driver.find_element(By.ID, "file")
    element.send_keys(file_path)
    submit_button = driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

    time.sleep(3)

    ###Конструкция для вывода числа из всплывающего окна
    alert = driver.switch_to.alert
    print("Число из всплывающего окна: ", alert.text.split()[-1])
    alert.accept()
finally:
    driver.quit()