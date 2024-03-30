import os
import string

import pytest
import time

from selenium.webdriver.common.by import By

from pageObjects.Different_Page_Objects.LoginPage import Login
from pageObjects.Different_Page_Objects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import random

class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()
    logger = LogGen.loggenerator()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        path = "C:\\PycharmProjects"
        dir_name = os.path.join(path, 'pythonProject1', 'Screenshots')
        full_name = os.path.join(dir_name, 'test_addCustomer_scr.png')
        self.logger.info("****************Test_003_AddCustomer********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.obj = Login(self.driver)  #Creating Object of Login Page for accessing different methods of login page
        self.obj.setUserName(self.username)
        self.obj.setPassword(self.password)
        self.obj.clickLogin()
        self.logger.info("****************Login successful********************")

        self.logger.info("***************Starting Add Customer Test**************")

        self.addcust = AddCustomer(self.driver) #Creating Object of Add Customer class
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomerMenuItem()

        self.addcust.clickOnAddnew()

        self.logger.info("***************Providing customer info**************")

        self.email = random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFname("Shilpi")
        self.addcust.setLname("Mukherjee")
        self.addcust.setGender("Male")
        self.addcust.setDOB("7/05/1985")  # Format: D/MM/YYYY
        self.addcust.setCompanyName("RocketSoftware")
        #self.addcust.setCustomerRoles("Guests")
        self.addcust.setCustomerRoles1("Guests")
        self.addcust.selectVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing purpose")
        self.addcust.clickOnSave()

        self.logger.info("****************** saving customer info ***************************")

        self.logger.info("************* Add customer validation started ***************")

        self.msg = self.driver.find_element(By.TAG_NAME, "body").text

        #print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*********** Add customer Test *************")
        else:
            self.driver.save_screenshot(os.path.normpath(full_name));
            self.logger.error('************ Add customer Test Failed *****************')
            assert True == False

        self.driver.close()
        self.logger.info("*************Ending Home Page Title Test ***************")


#This will give you 8 character string
def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    email_string = ''.join(random.choice(chars) for x in range(size))
    return email_string





