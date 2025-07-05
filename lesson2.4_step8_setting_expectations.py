from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math


link = "http://suninjuly.github.io/explicit_wait2.html"
driver = webdriver.Chrome()
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(link)
    WebDriverWait(driver, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'),'$100'))

    driver.find_element(By.ID, "book").click()

    x = driver.find_element(By.CSS_SELECTOR, "#input_value").text
    print("Число для формулы на странице: ", x)
    y = calc(x)
    answer = driver.find_element(By.CSS_SELECTOR, "#answer").send_keys(y)

    driver.find_element(By.ID, "solve").click()

    alert = driver.switch_to.alert
    print("Число из всплывающего окна: ", alert.text.split()[-1])
    alert.accept()
finally:
    driver.quit()