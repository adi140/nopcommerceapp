import pytest
from selenium import webdriver
from PageObject.LoginPage import loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseurl=ReadConfig.getApplicationURL()
    email=ReadConfig.getUserEmail()
    password=ReadConfig.getUserPassword()

    logger=LogGen.logfile()

    @pytest.mark.regression
    @pytest.mark.sanity

    def testhomepagetitle(self,setup):
        self.logger.info("********Test_001_Login***********")
        self.logger.info("***********Verifying Home page title **********")
        self.driver=setup
        self.driver.get(self.baseurl)
        url=self.driver.title
        if url=="Your store. Login":
             assert True
             self.logger.info("***********Home page title passed **********")
        else:
             assert False

    @pytest.mark.regression


    def testloginfunc(self,setup):
        self.logger.info("***********Verifying Login page  **********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=loginpage(self.driver)
        self.lp.setusername(self.email)
        self.lp.setpassword(self.password)
        self.lp.loginbuttonclick()
        check=self.driver.title
        if check=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("***********Login page verified **********")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "testloginfunc.png")
            print("problem is here")
            #self.driver.close()
            assert False




