"""
Positive test case for adding product based on price filter

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Adjust the filter by price between 150 and 450 rps
5) Now click on Filter button
6) User can view books only between 150 and 450 rps price
7) Add products to card
8) Check if products are added to card successfully.
"""

from selenium.webdriver import ActionChains
from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

class TestShoppingPrice(BaseClass):

    def test_shop_by_price_filter(self):
        log = self.getLogger()

        shop = MainPage(self.driver)
        shopping = shop.shopping()

        action = ActionChains(self.driver)
        left, right = shopping.getslider()
        action.drag_and_drop_by_offset(right, -28, 0).perform()

        min = shopping.getMinPrize().text
        max = shopping.getMaxPrize().text

        assert min == '₹150' and max == '₹451', "Min and max price are incorrect."

        shopping.getFilterbtn().click()

        products_prize = shopping.getproductsPrize()
        deleted_prize = shopping.deletedprice()

        deleted_items = []
        for delete in deleted_prize:
            deleted_items.append(delete.text)

        for prize in products_prize:
            if prize.text not in deleted_items:
                res = int(float((prize.text)[1:]))
                assert 150 <= res <= 450, "Price is not between 150 and 450, apply filter correctly."

        products = shopping.getProductname()

        log.info(" Add all products to card.")
        i = -1
        for product in products:
            i = i + 1
            shopping.addToCard()[i].click()

        checkout_page = shopping.viewCard()
        products = checkout_page.deleteProduct()
        assert len(products) != 0, "Products not inserted."
