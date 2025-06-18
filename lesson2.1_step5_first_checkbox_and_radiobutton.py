from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    x1 = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x1)
    input_1 = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    checkbox_1 = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    submit_button = driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()

    time.sleep(5)

    alert = driver.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    driver.quit()
