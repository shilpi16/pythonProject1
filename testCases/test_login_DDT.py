import os
import time

import pytest
from selenium import webdriver
from pageObjects.Different_Page_Objects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import XLUtils

class Test_002_DDT_Login:
    baseURL =  ReadConfig.getApplicationURL()
    path = "C:\\PycharmProjects"
    full_path = os.path.join(path, 'pythonProject1', 'TestData', 'LoginCreds.xlsx')

    logger = LogGen.loggenerator()


    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("**************** Test_002_DDT_Login*************")
        self.logger.info('***************** Verify DDT Login test *****************')
        self.driver = setup
        self.driver.get(self.baseURL)
        self.obj=Login(self.driver)
        self.rows = XLUtils.getRowCount(self.full_path, 'Sheet1')
        print("Number of rows in Excel:", self.rows)

        final_status=[];  # An empty list that will contain the final result

        for r in range(2, self.rows+1):  #It will run till row value = 5
            self.user = XLUtils.readData(self.full_path,'Sheet1',r,1)
            self.password = XLUtils.readData(self.full_path,'Sheet1',r,2)
            self.expected = XLUtils.readData(self.full_path,'Sheet1',r,3)
            self.obj.setUserName(self.user)
            self.obj.setPassword(self.password)
            self.obj.clickLogin()
            time.sleep(5)

            act_title=self.driver.title
            exp_title="Dashboard / nopCommerce administration"

            if act_title==exp_title:
                if self.expected=='Pass':
                    self.logger.info("***************Test Case is passed********")
                    self.obj.clickLogout()
                    final_status.append("Pass")
                elif self.expected=='Fail':
                     self.logger.info("***************Test Case is failed********")
                     self.obj.clickLogout()
                     final_status.append("Fail")

            elif act_title!=exp_title:
                if self.expected=='Fail':
                    self.logger.info("***************Test Case is Passed ********")
                    final_status.append("Pass")
                elif self.expected=='Pass':
                    self.logger.info("***************Test Case is Failed ********")
                    final_status.append("Fail")

        print(*final_status, sep = ", ")

        if "Fail" not in final_status:
            self.logger.info("***********Login DDT is Passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.info("***********Login DDT is Failed **********")
            self.driver.close()
            assert False

        self.logger.info("**********End of Login DDT Test **************")
        self.logger.info("******** Completed Test_002_DDT_Login***********")








