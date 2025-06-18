from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"
driver = webdriver.Chrome()

try:
    driver.get(link)

    treasure_box = driver.find_element(By.CSS_SELECTOR, "#treasure")
    valuex_tb = treasure_box.get_attribute("valuex")
    assert valuex_tb is not None

    y = calc(valuex_tb)
    input_1 = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)
    checkbox_1 = driver.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    radiobutton = driver.find_element(By.CSS_SELECTOR, "#robotsRule").click()
    submit_button = driver.find_element(By.CSS_SELECTOR, "body > div > form > div > div > button").click()

    time.sleep(5)

    alert = driver.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    driver.quit()
