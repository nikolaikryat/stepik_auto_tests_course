from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "https://suninjuly.github.io/text_input_task.html"

class TestMainPage():

    def setup_method(self):
        print("\nstart browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("\nquit browser for test..")
        self.browser.quit()

    def test_get_rest(self):
        self.browser.get(link)
        self.browser.implicitly_wait(5)
        self.browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys("get()")
        self.browser.find_element(By.CSS_SELECTOR, ".submit-submission").click()