"""
test case for adding product based on category

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Click on product category
5) User can view books only of particular category
6) if product is present then add to card.
7) Check if product is added to card successfully.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

valid_category_name = 'JavaScript'
product_name= "Functional Programming in JS"


class TestShoppingCategory(BaseClass):

    def test_shop_by_category_filter(self):
        log = self.getLogger()

        shop = MainPage(self.driver)
        shopping = shop.shopping()

        categories = shopping.getCategories()

        i = -1
        for category in categories:
            i = i+1
            if category.text == valid_category_name:
                shopping.getCategories()[i].click()
                break

        products = shopping.getProductname()
        log.info(" Add all products to card.")
        i = -1
        for product in products:
            i = i + 1
            if product_name == product.text:
                shopping.addToCard()[i].click()
                break


        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()= 'View Basket']")))

        checkout_page = shopping.viewCard()
        products = checkout_page.deleteProduct()
        assert len(products) != 0, "Products not inserted."
