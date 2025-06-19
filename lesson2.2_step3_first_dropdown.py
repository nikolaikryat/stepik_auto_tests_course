from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"
driver = webdriver.Chrome()

try:
    driver.get(link)

    first_number = driver.find_element(By.CSS_SELECTOR, "#num1").text
    second_number = driver.find_element(By.CSS_SELECTOR, "#num2").text
    sum = int(first_number) + int(second_number)
    print("Cумма двух чисел: ", sum)

    select = Select(driver.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(sum))
    submit_button = driver.find_element(By.CSS_SELECTOR, "body > div > form > button").click()
    time.sleep(10)

    alert = driver.switch_to.alert
    print("Число из всплывающего окна: ", alert.text.split()[-1])
    alert.accept()

finally:
    driver.quit()