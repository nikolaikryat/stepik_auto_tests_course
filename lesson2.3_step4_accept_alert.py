from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"
driver = webdriver.Chrome()

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(link)
    mag_jou_button = driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

    alert = driver.switch_to.alert
    alert.accept()

    x1 = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x1)
    input_1 = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    submit_button = driver.find_element(By.CSS_SELECTOR, "body > form > div > div > button").click()

    time.sleep(3)

    ###Конструкция для вывода числа из всплывающего окна
    alert = driver.switch_to.alert
    print("Число из всплывающего окна: ", alert.text.split()[-1])
    alert.accept()
finally:
    driver.quit()