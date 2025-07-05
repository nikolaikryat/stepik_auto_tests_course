from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "https://suninjuly.github.io/text_input_task.html"

@pytest.fixture
def browser():
        print("\nstart browser for test..")
        browser = webdriver.Chrome()
        yield browser
        print("\nquit browser..")
        browser.quit()

class TestMainPage():
    def test_get_rest(self, browser):
        browser.get(link)
        browser.implicitly_wait(5)
        browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys("get()")
        browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()

        alert = browser.switch_to.alert
        alert_text = ("Registration status message: ", alert.text)
        assert "Thank you for submitting the form!" in alert_text, f"Expected 'Thank you for submitting the form!' in result, but got: 'alert_text'"