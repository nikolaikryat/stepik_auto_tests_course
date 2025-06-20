from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "https://suninjuly.github.io/execute_script.html"
driver = webdriver.Chrome()

try:
    driver.get(link)

    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    print("Число для формулы на странице: ", x)
    y = calc(x)
    answer = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    checkbox_1 = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    driver.execute_script("window.scrollBy(0, 120);")
    radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    submit_button = driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    time.sleep(5)

    alert = driver.switch_to.alert
    print("Число из всплывающего окна: ", alert.text.split()[-1])
    alert.accept()
finally:
    driver.quit()