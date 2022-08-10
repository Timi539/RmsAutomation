import pytest
import time
from selenium import webdriver
from pageObjects.RMS.Candidate.CreateAccount import CreateAccount


class Test_Create_candidate_account:
    baseURL ="https://non-recurring-qa-rms.seamlesshiring.com/"
    firstname = "Oluwaseun"
    lastname = "Sunday"
    email = "Sunday@seamlesshr.com"
    password = "password"

    def test_createaccount(self,):
        self.driver = driver = webdriver.Chrome(executable_path="Driver/chromedriver")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.CA=CreateAccount(self.driver)
        time.sleep(10)
        self.CA.clickAccount()
        time.sleep(5)
        self.CA.setFirstname(self.firstname)
        time.sleep(5)
        self.CA.setLastname(self.lastname)
        time.sleep(5)
        self.CA.setEmail(self.email)
        time.sleep(5)
        self.CA.setPassword(self.password)
        time.sleep(5)
        self.CA.clickCreate()
        time.sleep(5)
        self.driver.close()

