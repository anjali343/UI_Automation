"""
positive test case

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Click on the Add To Basket button which adds that book to your basket
5) Go to checkout page.
6) Check if product is added to basket.
7) Delete product present in card.
8) Check card is empty after successful delete operation
"""

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

class TestAddDeleteProduct(BaseClass):

    def test_add_delete_particular_product_in_card(self):
        log = self.getLogger()

        shop = MainPage(self.driver)
        shopping = shop.shopping()

        products = shopping.getProductname()

        log.info(" Add products to card having Android into it.")
        i = -1
        for product in products:
            i = i + 1
            if 'Android Quick Start Guide' == product.text:
                shopping.addToCard()[i].click()

        products = shopping.getProductname()

        log.info(" Add all products to card.")
        i = -1
        for product in products:
            i = i + 1
            shopping.addToCard()[i].click()

        checkout_page = shopping.viewCard()
        products = checkout_page.deleteProduct()
        assert len(products) != 0, "Products not inserted."

