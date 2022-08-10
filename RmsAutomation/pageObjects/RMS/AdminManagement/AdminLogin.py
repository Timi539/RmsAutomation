import random
import string

class AdminLogin:
    admin_button_xpath= "/html/body/div[2]/div/section[1]/a"
    textbox_admin_email_id= "email"
    proceed_button_id= "submitLoginButton"
    textbox_admin_password_xpath= '//*[@id="passwordField"]/div[1]/input'

    def __init__(self, driver):
        self.driver = driver

    def adminButton(self):
        self.driver.find_element_by_xpath(self.admin_button_xpath).click()

    def setEmail(self, admin_email):
        self.driver.find_element_by_id(self.textbox_admin_email_id).clear()
        self.driver.find_element_by_id(self.textbox_admin_email_id).send_keys(admin_email)

    def clickProceed(self):
        self.driver.find_element_by_id(self.proceed_button_id).click()

    def setPassword(self, admin_password):
        #self.driver.find_element_by_xpath(self.textbox_admin_password_xpath)
        self.driver.find_element_by_xpath(self.textbox_admin_password_xpath).send_keys(admin_password)




#class AdminSetup:

