import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.card_product_page import Card_product_page
from pages.filter_page import Filter_page
from pages.main_page import Main_page
from pages.order_page import Order_page


def test_by_pr_no_auth_filters_one(set_up):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('log-level=3')
    # options.page_load_strategy = "eager"
    # options.add_experimental_option('excludeSwitches',['enable-logging'])
    # options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    print('Start Test: no auth one')
    no_auth_page = Main_page(driver)
    no_auth_page.main_page_select_filter_product()

    no_auth_filter_page = Filter_page(driver)
    no_auth_filter_page.filter_page_no_auth_buy()

    no_auth_cart_product_page = Card_product_page(driver)
    no_auth_cart_product_page.card_product_page_no_auth_buy()

    no_auth_order_page = Order_page(driver)
    no_auth_order_page.order_page_no_auth_buy()

    driver.quit()
