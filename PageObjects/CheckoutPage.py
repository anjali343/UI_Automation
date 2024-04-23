from selenium.webdriver.common.by import By


class CheckoutPage:
    """ All th locators and functions of checkout page are stored. """

    def __init__(self, driver):
        self.driver = driver

    product_remove = (By.XPATH, '//a[@class= "remove"]')
    product_name = (By.XPATH, '// td[@class = "product-name"]')

    def deleteProduct(self):
        return self.driver.find_elements(*CheckoutPage.product_remove)

    def getProductname(self):
        return self.driver.find_elements(*CheckoutPage.product_name)

