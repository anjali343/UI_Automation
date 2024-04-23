"""
Negative Test Cases

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter registered username in username textbox
5) Enter password in password textbox
6) Click on login button
7) User must successfully login to the web page
8) Click on Myaccount link which leads to Dashboard
9) Click on Address link
10) It must show error msg.
"""
import pytest

from PageObjects.MainPage import MainPage
from PageObjects.MyAccountDetailPage import MyAccountDetailPage
from TestData.AccountPageData import AccountPageData
from utilities.BaseClass import BaseClass

class TestEditAddress(BaseClass):
    """
    Negative Test Cases
    1)fristname_missing 2)lastname_missing 3)postcode_missing
    4)street_address_missing 5)city_missing
    """

    @pytest.fixture(scope='class')
    def user_login(self):
        login = MainPage(self.driver)
        loginpage = login.my_account_login()
        loginpage.getUsername().send_keys("kiran458")
        loginpage.getpassword().send_keys("Auto@54$23")
        loginpage.getCheckBox().click()
        loginpage.submit().click()

    @pytest.fixture(params=AccountPageData.invalid_address_data,
        ids = ["fristname_missing", "lastname_missing", "postcode_missing", "street_address_missing", "city_missing"])
    def getData(self, request):
        return request.param

    def test_edit_address_and_save(self, user_login, getData):
        log = self.getLogger()

        edt_address = MyAccountDetailPage(self.driver)
        edt_address.getAddress().click()
        edt_address.editBillingBtn().click()

        log.info("Edit billing address of user.")
        assert not edt_address.editBillingAddress(getData), "Billing Address is edited successfully."

        log.info("Edit shipping address of user.")
        edt_address.editShippingBtn().click()
        assert not edt_address.editShippingAddress(getData), "Shipping Address is edited successfully."
