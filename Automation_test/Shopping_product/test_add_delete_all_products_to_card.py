"""
positive test case

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Click on the Add To Basket button which adds that book to your basket
5) Go to checkout page.
6) Check if products are added to basket.
7) Delete all products present in card.
8) Check card is empty after successful delete operation
"""
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

class TestAddDeleteProducts(BaseClass):

    def test_add_delete_products_to_card(self):
        log = self.getLogger()

        self.driver.implicitly_wait(5)
        shop = MainPage(self.driver)
        shopping = shop.shopping()

        products = shopping.getProductname()

        log.info(" Add all products to card.")
        i = -1
        for product in products:
            i = i+1
            wait = WebDriverWait(self.driver, 5)
            wait.until(expected_conditions.presence_of_element_located((By.XPATH, '(//ul[@class = "products masonry-done"]/li/a)')))
            shopping.addToCard()[i].click()

        checkout_page = shopping.viewCard()
        products = checkout_page.deleteProduct()
        assert len(products) != 0, "Products not inserted."

        log.info("Delete All products present in card")
        delete_products = checkout_page.deleteProduct()

        i = len(products)
        for product in delete_products:
            i = i-1
            time.sleep(2)
            checkout_page.deleteProduct()[i].click()

        time.sleep(2)
        products = checkout_page.deleteProduct()
        assert len(products) == 0, "All products are not deleted"
