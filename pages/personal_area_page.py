from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import allure

from base.base import Base
from utilities.logger import Logger


class Personal_area_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    all_order_content = "//div[@class='right-contant account-content']/h1"
    personal_data_content = "//div[@class='right-contant']/h1"
    personal_data = "//*[@id='wrapper']/div[1]/div/div[1]/a[4]"
    name_user = "//input[@id='edit_firstname']"
    logo = "//*[@id='wrapper']/header/div[2]/div/div[1]/div[1]/a/img"

    # Getters
    def get_all_order_content(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.all_order_content)))

    def get_personal_data_content(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.personal_data_content)))

    def get_personal_data(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.personal_data)))

    def get_name_user(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.name_user)))

    def get_logo(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.logo)))
    # Action

    def select_personal_data(self):
        self.get_personal_data().click()

    def select_logo(self):
        self.get_logo().click()

    # Methodts

    def personal_area_page_steps(self):
        with allure.step("personal_area_page_steps"):
            Logger.add_start_step(method="personal_area_page_steps")
            self.assert_word(self.get_all_order_content(), "Все заказы")
            self.select_personal_data()
            self.assert_word(self.get_personal_data_content(), "Личные данные")
            self.select_logo()
            self.get_current_url()  # Получение ссылки страницы
            self.get_screenshot()  # Сделать скриншот
            Logger.add_end_step(url=self.driver.current_url, method="personal_area_page_steps")