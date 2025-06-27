from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        # link = "http://suninjuly.github.io/registration2.html"
        driver = webdriver.Chrome()
        driver.get(link)
        ###Заполнение обязательных полей
        first_name = driver.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input").send_keys("Ivan")
        last_name = driver.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input").send_keys("Ivanov")
        email = driver.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input").send_keys("ivan.ivanov@gmail.ru")

        ###Отправка заполненной формы
        button = driver.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)

        ###Нахождение элемента с текстом
        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        ###Запись в переменную текста
        welcome_text = welcome_text_elt.text

        ###Проверка, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element(By.XPATH, "//input[@placeholder='Введите имя']").send_keys("Ivan")
        input2 = browser.find_element(By.XPATH, "//input[@placeholder='Введите фамилию']").send_keys("Petrov")
        input3 = browser.find_element(By.XPATH, "//input[@placeholder='Введите Email']").send_keys("test@test.ru")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text, welcome_text_elt.text, "Поздравляем! Вы успешно зарегистировались!")

if __name__ == "__main__":
    unittest.main()