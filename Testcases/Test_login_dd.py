import pytest
from selenium import webdriver
from PageObject.LoginPage import loginpage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils
import time

class Test_002_DDT_Login:
    baseurl=ReadConfig.getApplicationURL()
    path=".//testdata/logindetails.xlsx"
    logger=LogGen.logfile()

    @pytest.mark.regression


    def testloginfunc(self,setup):
        self.logger.info("***********Verifying Login page  **********")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.lp=loginpage(self.driver)
        self.rows=XLUtils.getRowCount(self.path,'Sheet1')
        print("number of rows in an excel", self.rows)
        lst_status=[] #Empty list variable

        for r in range(2,self.rows+1):
            self.user=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path, 'Sheet1',r,2)
            self.expected=XLUtils.readData(self.path, 'Sheet1',r,3)

            self.lp.setusername(self.user)
            self.lp.setpassword(self.password)
            self.lp.loginbuttonclick()
            time.sleep(5)

            act_title=self.driver.title
            expected_title="Dashboard / nopCommerce administration"

            if act_title==expected_title:
                if self.expected=="Pass":
                    print("Test is working")
                    self.lp.logoutbuttonclick()
                    lst_status.append("Pass")
                    self.driver.save_screenshot(".\\screenshots\\" + "testloginfunc.png")
                    time.sleep(5)
                elif self.expected=="Fail":
                    print("cases are failed")
                    self.lp.logoutbuttonclick()
                    lst_status.append("Fail")
                    self.driver.save_screenshot(".\\screenshots\\" + "testloginfunc.png")
            elif act_title != expected_title:
                if self.expected == "Pass":
                    lst_status.append("Fail")
                elif self.expected == "Fail":
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            print("login ddt is passed")
            assert True
        else:
            print("login fails")
            assert False







