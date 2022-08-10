import time
from selenium import webdriver
from pageObjects.RMS.AdminManagement.CreateSpecialization import CreateSpecailization

class Test_specialization:
    baseURL = "https://non-recurring-qa-rms.seamlesshiring.com/"
    name = "Automation Specialization"


    def createSpecialisation(self, setup2):
        self.driver = webdriver.Chrome("Driver/chromedriver")
        self.driver.get(self.baseURL)
        self.driver = setup2
        self.CS=CreateSpecailization(self.driver)
        time.sleep(10)
        self.CS.jobtab()
        time.sleep(5)
        self.CS.specialization()
        time.sleep(5)
        self.CS.setName(self.name)
        time.sleep(5)
        self.CS.createButton()
        time.sleep(5)
        self.driver.close()

