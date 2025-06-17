from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_xpath_form"
driver = webdriver.Chrome()

try:
    driver.get(link)

    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")

    button = driver.find_element(By.XPATH, "/html/body/div/form/div[6]/button[3]").click()

    alert = driver.switch_to.alert
    print(alert.text.split()[-1])
    alert.accept()

finally:
    time.sleep(5)
    driver.quit()
