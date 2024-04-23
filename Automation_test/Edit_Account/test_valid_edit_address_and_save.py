"""
Positive Test Cases

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter registered username in username textbox
5) Enter password in password textbox
6) Click on login button
7) User must successfully login to the web page
8) Click on Myaccount link which leads to Dashboard
9) Click on Address link
10) User must view billing address and ship address
"""

from PageObjects.MainPage import MainPage
from PageObjects.MyAccountDetailPage import MyAccountDetailPage
from utilities.BaseClass import BaseClass

billing_address_data = {"firstname": "Akansha", "lastname": "Patil", "phone": "9326718923",
                "street-address": "Nagard road near saraswati school",
                "city": "Pune", "postcode": "418923", 'state': "Maharashtra"}

shipping_address_data = {"firstname": "Akansha", "lastname": "Patil", "phone": "8453216899",
                "street-address": "Nagard road near saraswati school",
                "city": "Pune", "postcode": "418923", 'state': "Maharashtra"}

class TestEditAddress(BaseClass):

    def test_edit_address_and_save(self):
        log = self.getLogger()

        login = MainPage(self.driver)
        loginpage = login.my_account_login()

        loginpage.getUsername().send_keys("anjalisolanke88")
        loginpage.getpassword().send_keys("Code!67890")
        loginpage.getCheckBox().click()
        loginpage.submit().click()

        alertText = loginpage.getSuccessMessage().text
        assert ("Hello" in alertText), "Error while login."

        edt_address = MyAccountDetailPage(self.driver)
        edt_address.getAddress().click()
        edt_address.editBillingBtn().click()

        log.info("Edit billing address of user.")
        assert edt_address.editBillingAddress(billing_address_data), "Billing Address is not edited successfully."

        log.info("Edit shipping address of user.")
        edt_address.editShippingBtn().click()
        assert edt_address.editShippingAddress(shipping_address_data), "Shipping Address is not edited successfully."
