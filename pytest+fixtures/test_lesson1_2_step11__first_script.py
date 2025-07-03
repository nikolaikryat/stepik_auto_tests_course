from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link = "https://suninjuly.github.io/text_input_task.html"

@pytest.fixture
def browser():
    print("\nstart driver for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()
class TestMainPage():

    def setup_method(self):
        print("start browser for test..")
        self.browser = webdriver.Chrome()

    def teardown_method(self):
        print("quit browser for test..")
        self.browser.quit()

    def test_get_rest(self):
    self.browser.get(link)
    self.browser.implicitly_wait(5)

    self.browser.find_element(By.CSS_SELECTOR, ".textarea").send_keys("get()")
    self.driver.find_element(By.CSS_SELECTOR, ".submit-submission").click()