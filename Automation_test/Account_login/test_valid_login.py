"""
Positive test case for account login.
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter registered username in username textbox
5) Enter password in password textbox
6) Click on login button
7) User must successfully login to the web page
"""
import pytest
from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass
from TestData.HomePageData import HomePageData


class TestLoginPage(BaseClass):

    @pytest.fixture(params=HomePageData.test_HomePage_data, ids=["Anjali", "Kiran"])
    def getData(self, request):
        return request.param

    def test_valid_login(self, getData):
        log = self.getLogger()

        login = MainPage(self.driver)
        loginpage = login.my_account_login()

        loginpage.getUsername().send_keys(getData["name_email"])
        loginpage.getpassword().send_keys(getData["password"])
        loginpage.getCheckBox().click()
        loginpage.submit().click()

        log.info("Check message after clicking on login button")
        alertText = loginpage.getSuccessMessage().text
        assert ("Hello" in alertText), "Error while login."
        loginpage.signOut().click()
