"""
Arrival test case:
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Now click on Home menu button
5) Test whether the Home page has Three Arrivals only
6) The Home page must contain only three Arrivals

Images in arrival should navigate:
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on Shop Menu
4) Now click on Home menu button
5) Test whether the Home page has Three Arrivals only
6) The Home page must contain only three Arrivals
7) Now click the image in the Arrivals
8) Test whether it is navigating to next page where the user can add that book into his basket.
9) Image should be clickable and should navigate to next page where user can add that book to his basket
"""

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def __init__(self):
        self.arrival = MainPage(self.driver)

    def test_count_slider_arrivals(self):
        arrivals = self.arrival.getArrivals()
        assert len(arrivals) == 3, "Count of arrivals are incorrect."

    def test_arrival_image_navigate_ruby_product(self):
        product = self.arrival.getImage()
        product.AddToBasket().click()
        product.ViewBasket().click()
        name = product.AddToBasket().text

        assert name == "Selenium Ruby", "Product is not added to basket."
