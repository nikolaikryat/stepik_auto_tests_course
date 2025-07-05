import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

class TestMainPage():
    def test_reg_form(self, browser):
        browser.get(link)

        browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
        browser.find_element(By.NAME, "last_name").send_keys("Petrov")
        browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
        browser.find_element(By.ID, "country").send_keys("Russia")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        alert = browser.switch_to.alert
        alert_text =  alert.text
        assert "Congrats, you've passed the task!" in alert_text, f"Expected 'Congrats, you've passed the task!' in result, but got: 'alert_text'"