import pytest
from selenium import webdriver

from pageObjects.RMS.Authentication.LoginPage import LoginPage
from pageObjects.RMS.AdminManagement.AdminLogin import AdminLogin
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import time






email = ReadConfig.getUseremail()
password = ReadConfig.getPassword()
logger = LogGen.loggen()
baseURL = ReadConfig.getApplicationURL()

admin_email = ReadConfig.getAdminemail()
admin_password = ReadConfig.getAdminpassword()
logger = LogGen.loggen()
baseURL = ReadConfig.getApplicationURL()

@pytest.fixture
def setup1():
    driver = webdriver.Chrome(executable_path="Driver/chromedriver")
    driver.get(baseURL)
    driver.implicitly_wait(60)
    driver.maximize_window()
    loginPage = LoginPage(driver)
    loginPage.setEmail(email)
    loginPage.setPassword(password)
    time.sleep(5)
    loginPage.clickLogin()
    #logger.info("************* Login successfull **********")
    yield driver
    driver.close()


@pytest.fixture
def setup2():
    driver = webdriver.Chrome(executable_path="Driver/chromedriver")
    driver.get(baseURL)
    driver.implicitly_wait(60)
    driver.maximize_window()
    adminLogin = AdminLogin(driver)
    adminLogin.adminButton()
    time.sleep(5)
    adminLogin.setEmail(admin_email)
    time.sleep(5)
    adminLogin.clickProceed()
    time.sleep(20)
    adminLogin.setPassword(admin_password)
    time.sleep(10)
    adminLogin.clickProceed()
    logger.info("************* Login successfull **********")
    #yield driver
    #driver.close()


####Pytest Html Report
##It is the hook for Adding Environment info to the HTML Report
def pytest_configure(config):
    config._metadata["Product Name"]= "Seamless RMS"

    config._metadata["QA Analyst"]="john"

#It is hook for deleting/modifying Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

# Generating reports command

#pytest -s -v --html=Reports/report.html testCases/ExitManagement/Admin/test_ExitReason.p
