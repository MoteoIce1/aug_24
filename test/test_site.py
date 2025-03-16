from selenium.webdriver.common.by import By
import time
from pages.homepage import Homepage
from pages.product import ProductPage


def test_open_s6(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_galaxy_s6()
    product_page = ProductPage(driver)
    product_page.check_title_is("Samsung galaxy s6")


def test_two_monitors(driver):
    homepage = Homepage(driver)
    homepage.open()
    homepage.click_monitor()
    time.sleep(2)
    print("Hi")
    homepage.check_products_count(2)
