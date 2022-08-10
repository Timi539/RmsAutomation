

class CreateSpecailization:
    job_tab_xpath= '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[3]/a'
    dropdown_specialization= '//*[@id="bs-example-navbar-collapse-1"]/ul[1]/li[3]/ul/li[2]/a'
    textbox_name_field_id= "name"
    create_button_xpath= '//*[@id="main-auth-entry"]/section/div/div[5]/div[2]/div/div/form/div[2]/button'

    def __init__(self, driver):
        self.driver = driver

    def jobtab(self):
        self.driver.find_element_by_xpath(self.job_tab_xpath).click()

    def specialization(self):
        self.driver.find_element_by_xpath(self.dropdown_specialization).click()

    def setName(self, admin_email):
        self.driver.find_element_by_id(self.textbox_name_field_id).clear()
        self.driver.find_element_by_id(self.textbox_name_field_id).send_keys(admin_email)

    def createButton(self):
        self.driver.find_element_by_xpath(self.create_button_xpath).click()
