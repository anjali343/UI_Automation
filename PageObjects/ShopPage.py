from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckoutPage


class ShopPage:
    """ All the locators and functions of shop page are stored. """

    def __init__(self, driver):
        self.driver = driver

    left_slider = (By.XPATH, "//div[@class='price_slider ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']//span[1]")
    right_slider = (By.XPATH, "//div[@class='price_slider ui-slider ui-corner-all ui-slider-horizontal ui-widget ui-widget-content']//span[2]")
    min_price = (By.XPATH, '//span[@class = "from"]')
    max_price = (By.XPATH, '//span[@class = "to"]')
    filter_button = (By.XPATH, "//button[normalize-space()='Filter']")
    products = (By.XPATH, '//ul[@class = "products masonry-done"]/li')
    products_price = (By.XPATH, "//span[@class='woocommerce-Price-amount amount']")
    deleted_price = (By.XPATH, '//span[@class= "price"]/del')
    product_names = (By.XPATH, '//ul[@class = "products masonry-done"]/li/a/h3')
    basket = (By.XPATH, "//a[text()= 'Add to basket']")
    view_basket = (By.XPATH, "//a[text()= 'View Basket']")
    card_content = (By.XPATH, "//span[@class = 'cartcontents']")
    category = (By.XPATH, "//ul[@class = 'product-categories']/li/a")


    def getslider(self):
        return self.driver.find_element(*ShopPage.left_slider), self.driver.find_element(*ShopPage.right_slider)

    def getMinPrize(self):
        return self.driver.find_element(*ShopPage.min_price)

    def getMaxPrize(self):
        return self.driver.find_element(*ShopPage.max_price)

    def getFilterbtn(self):
        return self.driver.find_element(*ShopPage.filter_button)

    def getproducts(self):
        return self.driver.find_elements(*ShopPage.products)

    def getproductsPrize(self):
        return self.driver.find_elements(*ShopPage.products_price)

    def deletedprice(self):
        return self.driver.find_elements(*ShopPage.deleted_price)

    def getProductname(self):
        return self.driver.find_elements(*ShopPage.product_names)

    def addToCard(self):
        return self.driver.find_elements(*ShopPage.basket)

    def viewCard(self):
        self.driver.find_element(*ShopPage.view_basket).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def cardsContent(self):
        self.driver.find_element(*ShopPage.card_content).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    def getCategories(self):
        return self.driver.find_elements(*ShopPage.category)
