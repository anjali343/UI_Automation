from selenium.webdriver.common.by import By


class RubyProductPage:
    """ All the locators and functions of home page ruby product are stored. """

    def __init__(self, driver):
        self.driver = driver

    addto_basket = (By.XPATH, "//button[normalize-space()='Add to basket']")
    view_basket = (By.XPATH, '//a[text()= "View Basket"]')
    product = (By.XPATH, '//a[text()= "Selenium Ruby"]')

    def AddToBasket(self):
        return self.driver.find_element(*RubyProductPage.addto_basket)

    def ViewBasket(self):
        return self.driver.find_element(*RubyProductPage.view_basket)

    def checkProductAdded(self):
        return self.driver.find_element(*RubyProductPage.product)
