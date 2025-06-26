import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "https://suninjuly.github.io/text_input_task.html"
driver = webdriver.Chrome()

try:
    driver.get(link)
    driver.implicitly_wait(5)

    textarea = driver.find_element(By.CSS_SELECTOR, ".textarea")
    textarea.send_keys("get()")

    submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")
    submit_button.click()
finally:
    driver.quit()