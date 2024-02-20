import allure

from base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Card_product_page(Base):
    url = 'https://luxury-flowers.ru/bouquets/bezmyatezhnost'  # Адресс главной страницы

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators (Локаторы)
    product_name = "//div[@class='product-right']/h1"
    product_price = "//*[@id='product']/div[2]/div[1]/div[2]/span[1]"
    buy_button = "//button[@id='button-cart']"
    placing_an_order = "//*[@id='popupcart_extended']/div[2]/div[2]/div[3]/button"
    placing_an_ordername = "//div[@class='name']/a"

    # Getters
    def get_product_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_name)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_buy_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.buy_button)))

    def get_placing_an_order(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.placing_an_order)))

    def get_placing_an_order_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.placing_an_ordername)))

    # Action

    def select_card_product(self):
        self.get_buy_button().click()

    def select_placing_an_order(self):
        self.get_placing_an_order().click()

    # Methodts

    def card_product_page_no_auth_buy(self):
        with allure.step("card_product_page_no_auth_buy"):
            Logger.add_start_step(method="card_product_page_no_auth_buy")
            self.assert_word(self.get_product_name(), "Малинки")
            self.get_screenshot()  # Сделать скриншот
            self.select_card_product()
            self.assert_word(self.get_placing_an_order_name(), "Малинки")
            self.select_placing_an_order()
            Logger.add_end_step(url=self.driver.current_url, method="card_product_page_no_auth_buy")

