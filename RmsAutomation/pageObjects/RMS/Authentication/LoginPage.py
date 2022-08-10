import pytest
from selenium import webdriver


class LoginPage:
    systemcontrol_button_xpath = "//a[normalize-space()='System Control']"
    email_field_xpath = "/html/body/div[2]/div/section[1]/div[1]/form/div[1]/div/input"
    password_field_xpath = "/html/body/div[2]/div/section[1]/div[1]/form/div[2]/div/input"
    login_button_xpath = "/html/body/div[2]/div/section[1]/div[1]/form/button"
    enter_company_xpath = "//*[@id='comapnysList']/div[2]/div[2]/button[1]"
    logout_of_company_xpath = "//*[@id='app']/div/aside/div/div[3]/div[1]/a[1]/img"
    confirmation_box_xpath = "//button[normalize-space()='Logout']"
    logout_of_app_xpath = "//a[normalize-space()='Log out of application']"
    Appconfirmation_box_xpath = "//button[normalize-space()='Logout']"
    company_list_xpath = "//*[@id='comapnysList']/div/div[1]/div[2]/div[1]"

    def __init__(self, driver):
        self.driver = driver

    def setEmail (self, email):
        self.driver.find_element_by_xpath(self.email_field_xpath).clear()
        self.driver.find_element_by_xpath(self.email_field_xpath).send_keys(email)

    def setPassword (self, password):
        self.driver.find_element_by_xpath(self.password_field_xpath).clear()
        self.driver.find_element_by_xpath(self.password_field_xpath).send_keys(password)

    def clickLogin(self):
        self.driver.find_element_by_xpath(self.login_button_xpath).click()