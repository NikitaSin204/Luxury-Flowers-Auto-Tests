import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base
from utilities.logger import Logger


# Если буду делать тест с авторизацией
class Login_page(Base):
    url = 'https://luxury-flowers.ru/login/'  # Адресс страницы авторизаци

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators (Локаторы для входа в систему)
    contetn_auth = "//div[@id='content']/h1"
    phone_user = "//input[@id='input-email']"
    password_user = "//input[@id='input-password']"
    login_button = "//input[@value='Войти']"

    # Getters

    def get_contetn_auth(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.contetn_auth)))

    def get_phone_user(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.phone_user)))

    def get_password_user(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.password_user)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.login_button)))

    # Action

    def insert_input_phone(self, user_phone):
        self.get_phone_user().send_keys(user_phone)
        print('Insert phone number into the field (Вставить номер телефона в поле)')

    def insert_input_password(self, user_password):
        self.get_password_user().send_keys(user_password)
        print('Insert password into the field (Вставить пароль в поле)')

    def select_login_button(self):
        self.get_login_button().click()
        print('Click login button (Клик по кнопке войти)')

    # Methodts

    def correct_authorization(self):
        with allure.step("correct_authorization"):
            Logger.add_start_step(method="correct_authorization")
            self.driver.get(self.url)
            self.driver.maximize_window()  # Сделать на весь экран
            self.get_current_url()  # Получение ссылки страницы
            self.assert_word(self.get_contetn_auth(), "Авторизация")
            self.get_screenshot()  # Сделать скриншот
            self.insert_input_phone("#")  # Не забыть стереть данные перед отправкой
            self.insert_input_password("#")  # Не забыть стереть данные перед отправкой
            self.select_login_button()  # Нажать кнопку "Войти"
            Logger.add_end_step(url=self.driver.current_url, method="correct_authorization")
