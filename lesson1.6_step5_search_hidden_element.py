from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


link = "http://suninjuly.github.io/find_link_text"
secret_link: str = str(math.ceil(math.pow(math.pi, math.e)*10000))
driver = webdriver.Chrome()

try:
    driver.get(link)
    text_link = driver.find_element(By.LINK_TEXT, secret_link)
    text_link.click()

    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    answer = driver.switch_to.alert.text
    print(answer)

finally:
    time.sleep(10)
    driver.quit()