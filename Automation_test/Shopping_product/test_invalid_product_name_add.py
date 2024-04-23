"""
Negative test case

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Try to add product which is not present in product list.
5) In checkout zero items will be there.
"""

import pytest
from selenium.webdriver.common.by import By

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

add_productdata = [{"product_name": ''}, {"product_name": "Java element"}]

class TestInvalidProductName(BaseClass):

    @pytest.mark.parametrize("name", add_productdata, ids=["empty_product_name", "incorrect_product_name"])
    def test_invalid_product_name_add(self, name):
        log = self.getLogger()

        shop = MainPage(self.driver)
        shopping = shop.shopping()

        products = shopping.getProductname()

        log.info(" Add all products to card having HTML into it.")
        i = -1
        for product in products:
            i = i + 1
            if name["product_name"] == product.text:
                shopping.addToCard()[i].click()

        card_item = self.driver.find_element(By.XPATH, "//span[@class = 'cartcontents']").text
        assert "0" in card_item
