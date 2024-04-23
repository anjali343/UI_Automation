from selenium.webdriver.common.by import By


class MyAccountDetailPage:
    """ All the locators and functions of account detail page are stored. """

    def __init__(self, driver):
        self.driver = driver

    address_btn = (By.XPATH, "//a[text()='Addresses']")
    billing_address = (By.XPATH, "//a[contains(@href,'billing')]")
    billing_firstname = (By.NAME, "billing_first_name")
    billing_lastname = (By.ID, "billing_last_name")
    billing_phone = (By.NAME, "billing_phone")
    billing_street_address = (By.NAME, "billing_address_1")
    billing_city = (By.NAME, "billing_city")
    billing_state = (By.XPATH, "(//ul[@id='select2-results-2'])[1]")
    billing_postcode = (By.NAME, "billing_postcode")
    save_address = (By.NAME, "save_address")
    verify_billing = (By.XPATH, "(//address)[1]")


    shipping_address = (By.XPATH, "//a[contains(@href,'shipping')]")
    shipping_firstname = (By.NAME, "shipping_first_name")
    shipping_lastname = (By.ID, "shipping_last_name")
    shipping_street_address = (By.NAME, "shipping_address_1")
    shipping_city = (By.NAME, "shipping_city")
    shipping_state = (By.XPATH, "(//ul[@id='select2-results-2'])[1]")
    shipping_postcode = (By.NAME, "shipping_postcode")
    verify_shipping = (By.XPATH, "(//address)[2]")

    error_msg = (By.XPATH, '//ul[@class = "woocommerce-error" ]/li')

    def getAddress(self):
        return self.driver.find_element(*MyAccountDetailPage.address_btn)

    def editBillingBtn(self):
        return self.driver.find_element(*MyAccountDetailPage.billing_address)

    def editShippingBtn(self):
        return self.driver.find_element(*MyAccountDetailPage.shipping_address)

    def getErrorMsg(self):
        return self.driver.find_element(*MyAccountDetailPage.error_msg)

    def editBillingAddress(self, input_data):
        """ Edit billing address.
        This Function will take input from test in the form of dictionary.
        If element is not none then it will edit the value or else it will keep the value as it is.
        If already value is present then it will clear the text and then it will edit.
        """
        fields = {
            MyAccountDetailPage.billing_firstname: "firstname",
            MyAccountDetailPage.billing_lastname: "lastname",
            MyAccountDetailPage.billing_phone: "phone",
            MyAccountDetailPage.billing_street_address: "street-address",
            MyAccountDetailPage.billing_city: "city",
            MyAccountDetailPage.billing_postcode: "postcode"
        }

        for element, key in fields.items():
            if input_data[key] is not None:
                field = self.driver.find_element(*element)
                field.clear()
                field.send_keys(input_data[key])

        self.driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
        self.driver.find_element(*MyAccountDetailPage.save_address).click()
        self.driver.find_element(*MyAccountDetailPage.address_btn).click()

        msg = self.driver.find_element(*MyAccountDetailPage.verify_billing).text

        if "not set up" in msg:
            return False
        else:
            return True

    def editShippingAddress(self, input_data):
        """
        Edit shipping address.
        This Function will take input from test in the form of dictionary.
        If element is not none then it will edit the value or else it will keep the value as it is.
        If already value is present then it will clear the text and then it will edit.
        """
        fields = {
            MyAccountDetailPage.shipping_firstname: "firstname",
            MyAccountDetailPage.shipping_lastname: "lastname",
            MyAccountDetailPage.shipping_street_address: "street-address",
            MyAccountDetailPage.shipping_city: "city",
            MyAccountDetailPage.shipping_postcode: "postcode"
        }

        for element, key in fields.items():
            if input_data[key] is not None:
                field = self.driver.find_element(*element)
                field.clear()
                field.send_keys(input_data[key])

        self.driver.execute_script('window.scrollBy(0, document.body.scrollHeight)')
        self.driver.find_element(*MyAccountDetailPage.save_address).click()
        self.driver.find_element(*MyAccountDetailPage.address_btn).click()

        msg = self.driver.find_element(*MyAccountDetailPage.verify_shipping).text

        if "not set up" in msg:
            return False
        else:
            return True
