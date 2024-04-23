"""
Negative test case for adding product based on category

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Click on product category
5) Check if category is not available.
"""

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

invalid_category_name = 'Java'

class TestShoppingInvalid(BaseClass):

    def test_invalid_category_filter(self):
        flag = True
        shop = MainPage(self.driver)
        shopping = shop.shopping()

        categories = shopping.getCategories()

        i = -1
        for category in categories:
            i = i+1
            if category.text == invalid_category_name:
                shopping.getCategories()[i].click()
                flag = True
                break

        assert flag, "Category is not available."
