"""
Positive test case for account login :- Data Driven Testing.
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter registered username in username textbox using excel file
5) Enter password in password textbox
6) Click on login button
7) if user is successfully login write passed in result column of Excel else write fail.
"""
from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass


class TestDataLoginPage(BaseClass):

    def test_data_driven_valid_login(self):
        log = self.getLogger()

        path = "E://Anjali_automation_project//Anjali_UI_Automation//TestData//test_data.xlsx"
        rows = self.getRowCount(path, 'login_details')
        for r in range(2, rows+1):
            username = self.readData(path, 'login_details', r, 1)
            password = self.readData(path, 'login_details', r, 2)

            login = MainPage(self.driver)
            loginpage = login.my_account_login()

            loginpage.getUsername().send_keys(username)
            loginpage.getpassword().send_keys(password)
            loginpage.getCheckBox().click()
            loginpage.submit().click()

            log.info("Check message after clicking on login button")
            alertText = loginpage.getSuccessMessage().text

            log.info("If login successfully write to result of excel file")
            if ("Hello" in alertText):
                self.writeData(path, "login_details", r, 3, "Test Passed")
                loginpage.signOut().click()
            else:
                self.writeData(path, "login_details", r, 3, "Test Failed")
