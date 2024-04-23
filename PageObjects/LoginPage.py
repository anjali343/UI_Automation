from selenium.webdriver.common.by import By


class LoginPage:
    """ All the locators and functions of login page are stored. """

    def __init__(self, driver):
        self.driver = driver

    username_edt = (By.NAME, "username")
    password_edt = (By.ID, "password")
    login_btn = (By.XPATH, '//input[@name = "login"]')
    remember_chk = (By.NAME, 'rememberme')
    forget_password = (By.LINK_TEXT, "Lost your password")
    success_msg = (By.XPATH, "//p[contains(text(),'Hello')]")
    error_msg = (By.XPATH, "//strong[normalize-space() = 'Error:']")
    sign_out = (By.XPATH, "//a[contains(text(),'Sign out')]")
    default_login_page = (By.XPATH, "//h2[normalize-space()='Login']")


    def getUsername(self):
        return self.driver.find_element(*LoginPage.username_edt)

    def getpassword(self):
        return self.driver.find_element(*LoginPage.password_edt)

    def getCheckBox(self):
        return self.driver.find_element(*LoginPage.remember_chk)

    def submit(self):
        return self.driver.find_element(*LoginPage.login_btn)

    def forgetpassword(self):
        return self.driver.find_element(*LoginPage.forget_password)

    def getSuccessMessage(self):
        return self.driver.find_element(*LoginPage.success_msg)

    def getErrorMsg(self):
        return self.driver.find_element(*LoginPage.error_msg)

    def signOut(self):
        return self.driver.find_element(*LoginPage.sign_out)

    def defaultLogin(self):
        return self.driver.find_element(*LoginPage.default_login_page)
