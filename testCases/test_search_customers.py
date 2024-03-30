import os
import string

import time
import pytest
from pageObjects.Different_Page_Objects.LoginPage import Login
from pageObjects.Different_Page_Objects.AddCustomerPage import AddCustomer
from pageObjects.Different_Page_Objects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggenerator() #Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        emailId = 'victoria_victoria@nopCommerce.com'
        column_email = 'Email'
        path = "C:\\PycharmProjects"
        dir_name = os.path.join(path, 'pythonProject1', 'Screenshots')
        full_name = os.path.join(dir_name, 'search_cust_by_email_scr.png')
        self.logger.info("****************Test_001_Search_Customer_by_email********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.obj = Login(self.driver)  #Creating Object of Login Page for accessing different methods of login page
        self.obj.setUserName(self.username)
        self.obj.setPassword(self.password)
        self.obj.clickLogin()
        self.logger.info("****************Login successful********************")

        self.logger.info("***************Starting Search Customer By Email **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("************starting Search Customer By EmailID ***********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setEmail(emailId)
        searchcust.clickSearch()
        time.sleep(2)
        status =searchcust.searchCustomer_By_col_name(column_email, emailId )
        assert True==status
        self.logger.info("***************TC_SearchCustomerByEmail_Finished *****************")
        self.driver.close()

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        fname = 'Victoria'
        lname = 'Terces'
        full_name = fname+" "+lname
        column_name = 'Name'
        path = "C:\\PycharmProjects"
        dir_name = os.path.join(path, 'pythonProject1', 'Screenshots')
        full_path = os.path.join(dir_name, 'search_cust_by_name_scr.png')
        self.logger.info("****************Test_002_Search_Customer_by_name********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.obj = Login(self.driver)  #Creating Object of Login Page for accessing different methods of login page
        self.obj.setUserName(self.username)
        self.obj.setPassword(self.password)
        self.obj.clickLogin()
        self.logger.info("****************Login successful********************")

        self.logger.info("***************Starting Search Customer By Name **********")
        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.logger.info("************starting Search Customer By Name ***********")
        searchcust = SearchCustomer(self.driver)
        searchcust.set_fname(fname)
        searchcust.set_lname(lname)
        searchcust.clickSearch()
        time.sleep(2)
        status =searchcust.searchCustomer_By_col_name(column_name, full_name)
        assert True==status
        self.logger.info("***************TC_SearchCustomerByName_Finished *****************")
        self.driver.close()



