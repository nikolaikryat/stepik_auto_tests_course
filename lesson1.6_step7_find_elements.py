from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    elements = driver.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Мой ответ")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    alert = driver.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(5)
    driver.quit()