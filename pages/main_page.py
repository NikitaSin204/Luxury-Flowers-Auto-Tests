import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from base.base import Base
from utilities.logger import Logger


class Main_page(Base):
    url = 'https://luxury-flowers.ru/'  # Адресс главной страницы

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators (Локаторы главной страницы)

    contetn_main_page = "//div[@class='home-title']/h1"  # Заголовок на главной странице странице
    buy_button = "//button[@data-product_id='74']"  # Кнопка "купить" на главной странице
    buy_button_card = "//button[@id='button-cart']"  # Кнопка "купить" в карточке товара
    placing_button = "//*[@id='popupcart_extended']/div[2]/div[2]/div[3]/button"  # Кнопка "оформление заказа"
    filter_price = "//*[@id='wrapper']/div[4]/div/div[1]/div[2]/div[2]/a[2]"  # Фильтр стоимости

    # Getters
    def get_content_main(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.contetn_main_page)))

    def get_contetn_filter(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    def get_filter_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_price)))

    # Action
    def select_filter_price(self):
        self.get_filter_price().click()

    # Methodts
    def main_page_select_filter_product(self):
        with allure.step("main_page_select_filter_product"):
            Logger.add_start_step(method="main_page_select_filter_product")
            self.driver.get(self.url)
            self.driver.maximize_window()  # Сделать на весь экран
            self.get_current_url()  # Получение ссылки страницы
            self.assert_word(self.get_content_main(), "Доставка свежих цветов в Самаре")
            self.assert_word(self.get_contetn_filter(), "# 2000 Р - 3000 Р")
            self.get_screenshot()  # Сделать скриншот
            self.select_filter_price()
            Logger.add_end_step(url=self.driver.current_url, method="main_page_select_filter_product")
