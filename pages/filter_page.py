import allure
from selenium.webdriver import ActionChains

from base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Filter_page(Base):
    url = 'https://luxury-flowers.ru/price/ot-2000-do-3000-rub/'  # Адресс страницы

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    filter_content = "//div[@class='category-top']/h1"
    product_buy = "//*[@id='content']/div[3]/div/div[1]/div/div[2]/div/div[3]/button[1]"
    product_buy_name = "//*[@id='content']/div[3]/div/div[1]/div/div[2]/div/div[1]/a"
    price_slider = "//*[@id='slider-range']/a[2]"
    # Getters
    def get_filter_content(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_content)))

    def get_product_buy_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_buy_name)))

    def get_product_buy(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.product_buy)))

    def get_price_slider(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.price_slider)))

    # Action

    def action_price_slider(self):
        price_slider = self.get_price_slider()
        actions = ActionChains(self.driver)
        actions.click_and_hold(price_slider).move_by_offset(-50, 0).release().perform()

    def select_filter_price(self):
        self.get_product_buy().click()

    # Methodts
    def filter_page_no_auth_buy(self):
        with allure.step("personal_area_page_steps"):
            Logger.add_start_step(method="filter_page_no_auth_buy")
            self.get_current_url()  # Получение ссылки страницы
            self.assert_word(self.get_filter_content(), "Доставка букетов от 2000 до 3000 рублей в Самаре")
            self.action_price_slider()
            self.assert_word(self.get_product_buy_name(), "Малинки")
            self.get_screenshot()  # Сделать скриншот
            self.select_filter_price()
            Logger.add_end_step(url=self.driver.current_url, method="filter_page_no_auth_buy")
