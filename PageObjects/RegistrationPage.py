from selenium.webdriver.common.by import By


class RegistrationPage:
    """ All the locators and functions of register page are stored. """

    def __init__(self, driver):
        self.driver = driver

    reg_email = (By.ID, "reg_email")
    reg_password = (By.ID, "reg_password")
    register_btn = (By.NAME, "register")
    success_msg = (By.XPATH, "//p[contains(text(),'Hello')]")
    error_msg = (By.XPATH, "//div[@id='body']//li[1]")
    sign_out = (By.XPATH, "//a[contains(text(),'Sign out')]")

    def getUsername(self):
        return self.driver.find_element(*RegistrationPage.reg_email)

    def getpassword(self):
        return self.driver.find_element(*RegistrationPage.reg_password)

    def submit(self):
        return self.driver.find_element(*RegistrationPage.register_btn)

    def getSuccessMessage(self):
        return self.driver.find_element(*RegistrationPage.success_msg)

    def getErrorMsg(self):
        return self.driver.find_element(*RegistrationPage.error_msg)

    def signOut(self):
        return self.driver.find_element(*RegistrationPage.sign_out)
