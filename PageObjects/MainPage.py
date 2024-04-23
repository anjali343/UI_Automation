from selenium.webdriver.common.by import By
from PageObjects.CheckoutPage import CheckoutPage
from PageObjects.LoginPage import LoginPage
from PageObjects.RegistrationPage import RegistrationPage
from PageObjects.RubyProductPage import RubyProductPage
from PageObjects.ShopPage import ShopPage


class MainPage:
    """
    All the locators and functions of main page are stored.
    this is the first page user will see after opening the site.
    """

    def __init__(self, driver):
        self.driver = driver

    account_login = (By.XPATH, "//a[text()='My Account']")
    shop_page = (By.XPATH, '//a[text()= "Shop"]')
    arrivals = (By.XPATH, '//ul[@class= "products"]')
    ruby_img = (By.XPATH, "//img[@title='Selenium Ruby']")
    view_basket = (By.XPATH, "//i[@class='wpmenucart-icon-shopping-cart-0']")

    def my_account_login(self):
        self.driver.find_element(*MainPage.account_login).click()
        login_page = LoginPage(self.driver)
        return login_page

    def my_account_registration(self):
        self.driver.find_element(*MainPage.account_login).click()
        registration_page = RegistrationPage(self.driver)
        return registration_page

    def shopping(self):
        self.driver.find_element(*MainPage.shop_page).click()
        shop_page = ShopPage(self.driver)
        return shop_page

    def getArrivals(self):
        return self.driver.find_elements(*MainPage.arrivals)

    def getImage(self):
        self.driver.find_element(*MainPage.ruby_img).click()
        product_page = RubyProductPage(self.driver)
        return product_page

    def viewCard(self):
        self.driver.find_element(*MainPage.view_basket).click()
        checkout_page = CheckoutPage(self.driver)
        return checkout_page
