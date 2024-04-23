"""
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter the case changed username in username textbox
5) Enter the case changed password in the password textbox
6) Now click on login button
7) Once you are logged in, sign out of the site
8) Now press back button
9) User shouldn’t be signed in to his account rather a general webpage must be visible
"""

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

class TestSignOut(BaseClass):

    def test_sign_out(self):
        log = self.getLogger()

        login = MainPage(self.driver)
        loginpage = login.my_account_login()

        loginpage.getUsername().send_keys("anjalisolanke88")
        loginpage.getpassword().send_keys("Code!67890")
        loginpage.getCheckBox().click()
        loginpage.submit().click()
        alertText = loginpage.getSuccessMessage().text
        assert ("Hello" in alertText), "Error while login."
        log.info("Login is successfully.")

        loginpage.signOut().click()
        log.info("You are sign out successfully.")

        default_page = loginpage.defaultLogin().text
        assert default_page == "Login", "User not sign out."
