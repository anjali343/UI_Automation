"""
Test Cases: Data Driven

1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter registered username in username textbox
5) Enter password in password textbox
6) Click on login button
7) User must successfully login to the web page
8) Click on Myaccount link which leads to Dashboard
9) Click on Address link
10) Take data from excel and it must show warning msg.
"""

from PageObjects.MainPage import MainPage
from PageObjects.MyAccountDetailPage import MyAccountDetailPage
from utilities.BaseClass import BaseClass


class TestDataDivenEditAddress(BaseClass):

    def test_data_driven_invalid_edit_address(self):
        log = self.getLogger()

        path = "E://Anjali_automation_project//Anjali_UI_Automation//TestData//test_data.xlsx"
        rows = self.getRowCount(path, 'login_details')

        for r in range(3, rows+1):
            log.info("Read username and password from Excel file")
            username = self.readData(path, 'login_details', r, 1)
            password = self.readData(path, 'login_details', r, 2)

            login = MainPage(self.driver)
            loginpage = login.my_account_login()

            loginpage.getUsername().send_keys(username)
            loginpage.getpassword().send_keys(password)
            loginpage.getCheckBox().click()
            loginpage.submit().click()

            alertText = loginpage.getSuccessMessage().text
            assert ("Hello" in alertText), "Error while login."

            address_data  = self.formDictionary(path, 'invalid_edit_address')

            for address in address_data:
                edt_address = MyAccountDetailPage(self.driver)
                edt_address.getAddress().click()
                edt_address.editBillingBtn().click()

                log.info("Edit billing address of user.")
                assert not edt_address.editBillingAddress(address), "Billing Address edited successfully."
