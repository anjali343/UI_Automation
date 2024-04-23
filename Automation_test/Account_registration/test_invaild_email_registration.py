"""
Negative test cases for registration
1] Gmail address is incorrect, '@gmail.com' is not present.
2] Empty Password and correct email id.
3] Empty email and correct password.
4] Empty email and empty password.
"""

import pytest
from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

registration_data = [{"email":"anjalislanke", "password":"Auto@54$23"}, {"email":"ABGXET@gmail.com", "password":""},
                     {"email":"", "password":"t4jn8nfrg"}, {"email":"", "password":""}]


class TestInvalidRegistration(BaseClass):

    @pytest.mark.parametrize('input_data', registration_data,
                             ids= ["incorrect_email", "Empty_Password", "Empty_email", "Empty_email_password"])

    def test_invalid_registration(self, input_data):
        log = self.getLogger()

        registration = MainPage(self.driver)
        registrationpage = registration.my_account_registration()

        registrationpage.getUsername().send_keys(input_data['email'])
        registrationpage.getpassword().send_keys(input_data['password'])
        registrationpage.submit().click()

        log.info("Check if email address is valid, any warning message is displayed.")
        warning_msg = registrationpage.getUsername().get_attribute("validationMessage")
        if warning_msg == '':
            error_msg = registrationpage.getErrorMsg().text
            assert ("Error: Please" in error_msg)
        else:
            assert ("Please include an '@' in the email address" in warning_msg)
