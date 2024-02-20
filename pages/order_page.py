import time

import allure
from selenium.webdriver.support.ui import Select

from base.base import Base
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from utilities.logger import Logger


class Order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators (Локаторы заказа)

    content_cart_no_auth = "//div[@class='right-contant']/h1"  # Заголовок на странице корзины
    your_name = "//input[@id='customer_firstname']"  # Ваше имя
    postcard_text = "//textarea[@id='customer_field39']"  # Текст открытки
    customer_phone = "//input[@id='customer_telephone']"  # телефон
    customer_email = "//input[@id='customer_email']"  # Электронную почту
    receiver_name = "//input[@id='shipping_address_field26']"  # Имя получателя
    receiver_phone = "//input[@id='shipping_address_field20']"  # Телефон получателя
    address = "//input[@id='shipping_address_field26']"  # Адресс доставки
    room = "//input[@id='shipping_address_apartment']"  # Квартира
    entrance = "//input[@id='shipping_address_entrance']"  # Подъезд
    floor = "//input[@id='shipping_address_floor']"  # квартира
    order_price_product = "//*[@id='simplecheckout_cart']/div[1]/div/div/div[4]/div/span"
    calendar_date = "//input[@id='shipping_address_field21']"
    calendar_day = ("/html/body/div[6]/div/div[1]/table/tbody/tr[4]/td[5]")
    comment = "//textarea[@id='comment']"
    select_time_one = "//select[@id='shipping_address_field27']"
    select_time_two = "//select[@id='shipping_address_field28']"

    # Getters
    def get_content_cart_no_auth(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.content_cart_no_auth)))

    def get_order_price_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.order_price_product)))

    def get_postcard_text(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.postcard_text)))

    def get_your_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.your_name)))

    def get_customer_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.customer_phone)))

    def get_customer_email(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.customer_email)))

    def get_receiver_name(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.receiver_name)))

    def get_receiver_phone(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.receiver_phone)))

    def get_address(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.address)))

    def get_room(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.room)))

    def get_entrance(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.entrance)))

    def get_floor(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.floor)))

    def get_calendar_date(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.calendar_date)))

    def get_calendate_day(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.calendar_day)))

    def get_comment(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.comment)))

    def get_select_time_one(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_time_one)))

    def get_select_time_two(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_time_two)))

    # Action
    def insert_input_postcard_text(self, cart_text):
        self.get_postcard_text().send_keys(cart_text)

    def insert_input_your_name(self, your_name):
        self.get_your_name().send_keys(your_name)

    def insert_input_customer_phone(self, customer_phone):
        self.get_customer_phone().send_keys(customer_phone)

    def insert_input_customer_email(self, customer_email):
        self.get_customer_email().send_keys(customer_email)

    def insert_input_receiver_name(self, receiver_name):
        self.get_receiver_name().send_keys(receiver_name)

    def insert_input_receiver_phone(self, receiver_phone):
        self.get_receiver_phone().send_keys(receiver_phone)

    def insert_input_address(self, address):
        self.get_address().send_keys(address)

    def insert_input_room(self, room):
        self.get_room().send_keys(room)

    def insert_input_entrance(self, entrance):
        self.get_entrance().send_keys(entrance)

    def insert_input_floor(self, floor):
        self.get_floor().send_keys(floor)

    def insert_calendar_dater(self):
        self.get_calendar_date().click()

    def insert_calendate_day(self):
        self.get_calendate_day().click()

    def insert_textarea_comment(self, comment):
        self.get_comment().send_keys(comment)

    def select_time_d_one(self, value):
        select = Select(self.get_select_time_one())
        select.select_by_value(value)

    def select_time_d_two(self, value):
        select = Select(self.get_select_time_two())
        select.select_by_value(value)

    def select_order_price_product(self):
        price_pr = self.get_order_price_product().text
        return price_pr

    # Methodts

    def order_page_no_auth_buy(self):
        with allure.step("order_page_no_auth_buy"):
            Logger.add_start_step(method="order_page_no_auth_buy")
            self.get_current_url()  # Получение ссылки страницы
            self.assert_word(self.get_content_cart_no_auth(), "Ваш заказ")
            self.assert_word(self.get_order_price_product(), self.select_order_price_product())
            self.insert_input_postcard_text("Мор амур")
            name = self.generate_random_name()
            self.insert_input_your_name(name)
            phone_number = self.generate_random_phone_number()  # Генерация случайного номера телефона
            self.insert_input_customer_phone(phone_number)  # Передача номера телефона
            self.insert_input_customer_email('adsas@mail.ru')
            self.insert_input_receiver_name(name)
            self.insert_input_receiver_phone(phone_number)  # Передача номера телефона
            self.insert_input_address('ул.Гагарина 144')
            self.insert_input_room("421")
            self.insert_input_entrance("2")
            self.insert_input_floor("13")
            self.insert_calendar_dater()
            self.insert_calendate_day()
            time.sleep(20)
            self.select_time_d_one("7")
            self.select_time_d_two("13")
            self.insert_textarea_comment("asdasdasdasdasdasdasdasdasdasdasdas")
            self.get_screenshot()  # Сделать скриншот
            time.sleep(5)
            Logger.add_end_step(url=self.driver.current_url, method="order_page_no_auth_buy")
