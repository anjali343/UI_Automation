"""
Positive test cases for account registration.
1) Open the browser
2) Enter the URL “http://practice.automationtesting.in/”
3) Click on My Account Menu
4) Enter registered Email Address in Email-Address textbox
5) Enter your own password in password textbox
6) Click on Register button
7) User will be registered successfully and will be navigated to the Home page
"""

import pytest
from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

registration_data = [("kira78@gmail.com", "Auto@54$23"),
                     ("Rertycr6@gmail.com", "Agr42189@4")]


class TestRegistration(BaseClass):

    @pytest.mark.parametrize('email, password', registration_data)
    def test_valid_registration(self, email, password):
        log = self.getLogger()

        registration = MainPage(self.driver)
        registrationpage = registration.my_account_registration()

        registrationpage.getUsername().send_keys(email)
        registrationpage.getpassword().send_keys(password)
        registrationpage.submit().click()

        log.info("After clicking of register button check message displayed.")
        alertText = registrationpage.getSuccessMessage().text
        assert ("Hello" in alertText), "Error while registration."
        registrationpage.signOut().click()

