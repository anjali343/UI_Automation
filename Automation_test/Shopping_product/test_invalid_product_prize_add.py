"""
Negative test case

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Try to add product having price less than 150 or more than 500
5) In checkout zero items will be there.
"""

import pytest
from selenium.webdriver.common.by import By

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

add_productdata = [{"product_price": '120'}, {"product_price": "650"}]

class TestInvalidProductPrice(BaseClass):

    @pytest.mark.parametrize("price", add_productdata, ids=["Less_Price", "Price_exceeded"])
    def test_invalid_product_price_add(self, price):
        log = self.getLogger()

        shop = MainPage(self.driver)
        shopping = shop.shopping()

        products = shopping.getProductname()

        log.info(" Add all products to card having HTML into it.")

        products_price = shopping.getproductsPrize()
        prices = []
        for product in products_price:
            prices.append(product.text)

        i = -1
        for product in products:
            i = i + 1
            if price["product_price"] in prices:
                shopping.addToCard()[i].click()

        card_item = self.driver.find_element(By.XPATH, "//span[@class = 'cartcontents']").text
        assert "0" in card_item
