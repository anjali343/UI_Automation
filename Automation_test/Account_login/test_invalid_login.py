"""
Negative Test Cases for login

1. Empty password and correct username.
2. Empty username and correct password.
3. Incorrect username and incorrect password.
4. Empty username and empty password.
5. Case sensitivity is checked.

All five tests are added using parametrization.
"""

import pytest
from PageObjects.MainPage import MainPage
from utilities.BaseClass import BaseClass

login_data = [{"username":"anjalisolanke88", "password":""}, {"username":"", "password":"Code!67890"}, {"username":"ABC", "password": "XYZ"},
              {"username":'', "password":''}, {"username":"ANJALISOLANKE88", "password": "CODE!67890"}]

class TestInvalidLogin(BaseClass):

    @pytest.mark.parametrize('input_data', login_data, ids=["Empty_password", "Empty_username",
                                    "Incorrect_username_password", "Empty_username_password", "Case_sensitive"])
    def test_invalid_login(self, input_data):
        log = self.getLogger()

        login = MainPage(self.driver)
        loginpage = login.my_account_login()

        log.info("Login using given username and password")
        loginpage.getUsername().send_keys(input_data["username"])
        loginpage.getpassword().send_keys(input_data["password"])
        loginpage.getCheckBox().click()
        loginpage.submit().click()

        log.info("Check if error message is displayed.")

        alertText = loginpage.getErrorMsg().text
        assert ("Error:" in alertText), "Login Successfully."
