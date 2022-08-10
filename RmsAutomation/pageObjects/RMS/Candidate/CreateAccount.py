
class CreateAccount:
    button_create_an_account_xpath= "/html/body/div[2]/div[1]/section[1]/div[1]/div[1]/a[2]"
    textbox_firstname_xpath= "/html/body/div[2]/div/section[1]/form/div[4]/div/input"
    textbox_lastname_xpath= "/html/body/div[2]/div/section[1]/form/div[5]/div/input"
    textbox_email_xpath= "/html/body/div[2]/div/section[1]/form/div[6]/div/input"
    textbox_password_xpath= "/html/body/div[2]/div/section[1]/form/div[7]/div/input"
    button_create_account_xpath= "/html/body/div[2]/div/section[1]/form/button"

    def __init__(self,driver):
        self.driver=driver

    def clickAccount(self):
        self.driver.find_element_by_xpath(self.button_create_an_account_xpath).click()

    def setFirstname(self,firstname):
        self.driver.find_element_by_xpath(self.textbox_firstname_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_firstname_xpath).send_keys(firstname)

    def setLastname(self,lastname):
        self.driver.find_element_by_xpath(self.textbox_lastname_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_lastname_xpath).send_keys(lastname)

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.textbox_email_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_email_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).clear()
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(password)

    def clickCreate(self):
        self.driver.find_element_by_xpath(self.button_create_account_xpath).click()