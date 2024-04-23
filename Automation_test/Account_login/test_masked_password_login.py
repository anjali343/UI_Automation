"""
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter the password field with some characters.
5) The password field should display the characters in asterisks that means type should be password.
"""

from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

class TestMaskedPassword(BaseClass):

    def test_masked_password(self):
        log = self.getLogger()

        login = MainPage(self.driver)
        loginpage = login.my_account_login()

        loginpage.getpassword().send_keys("Code!67890")

        log.info("Check type of password.")
        passwrd = loginpage.getpassword().get_attribute('type')

        log.info("Take screenshot to verify that password is not visible")
        self.driver.get_screenshot_as_file("masked_password.png")

        assert passwrd == 'password', "Password is not masked."
