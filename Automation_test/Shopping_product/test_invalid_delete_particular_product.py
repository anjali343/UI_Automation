"""
Negative test case

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Click on the Add To Basket button which adds that book to your basket
5) Proceed to checkout.
6) No element is present so can't delete OR Different element is given.

"""
import pytest
from selenium.webdriver.common.by import By

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

delete_data = [{"product_name": ''}, {"product_name": "Java element"}]

class TestInvalidDeleteProduct(BaseClass):

    @pytest.mark.parametrize("name", delete_data, ids=["empty_product_name", "incorrect_product_name"])
    def test_invalid_delete_product_from_card(self, name):
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

        card = self.driver.find_element(By.XPATH, "//span[@class = 'cartcontents']").text
        assert '0' in card, "Item is present in card"
