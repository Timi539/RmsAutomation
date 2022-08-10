from selenium import webdriver

class CandidateLogin:
    textbox_email_xpath="//body/div[2]/div[1]/section[1]/div[1]/form[1]/div[1]/div[1]/input[1]"
    textbox_password_xpath="//body/div[2]/div[1]/section[1]/div[1]/form[1]/div[2]/div[1]/input[1]"
    button_login_xpath="//button[contains(text(),'Log in to your account')]"
    link_logout_xpath="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element_by_xpath(self.link_logout_xpath).click()
