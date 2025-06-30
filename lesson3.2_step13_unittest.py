from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def fill_form(link):
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, ".first:required").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, ".second:required").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, ".third:required").send_keys("url@gmail")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    return browser.find_element(By.TAG_NAME, "h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    unittest.main()