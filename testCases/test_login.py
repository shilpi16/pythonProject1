import os

import pytest
from selenium import webdriver
from pageObjects.Different_Page_Objects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

# We need to import this LoginPage module from Page objecs because all the action methods are loacted in some other package
# Remember to access the class variable we need to use 'self' keyword
# Keep all the duplications in one fixture under conftest file. Example we are creating driver in every test case
# Here setup is a fixture

class Test_001_Login:
    #baseURL = "https://admin-demo.nopcommerce.com" # We ccan't use hardcoded values in test classes, we need to read it from the utilities
    baseURL =  ReadConfig.getApplicationURL() #Accessing the static method using classname
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.loggenerator()


    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        path = "C:\\PycharmProjects"
        dir_name = os.path.join(path, 'pythonProject1', 'Screenshots')
        full_name = os.path.join(dir_name, 'test_homepagetitle.png')
        self.logger.info("**************** Test_001_Login ***************")
        self.logger.info('***************** Verify Home Page Title *****************')
        #self.driver = webdriver.Chrome() # Initializing the chrome driver. Since this is repeatable, we need to keep this in a fixture inside conftest file
        self.driver = setup # Initializing the chrome driver using setup fixture
        self.driver.get(self.baseURL) # Launching the base url
        actual_title = self.driver.title
        expected_title = "Your store. Login"
        if actual_title == expected_title:
            assert True
            self.driver.close()  # Closing the chrome driver
            self.logger.info('************ Home page title test is passed *****************')
        else:
            #How to take screenshot
            self.driver.save_screenshot(os.path.normpath(full_name));
            assert False
            self.driver.close()
            self.logger.error('************ Home page title test is failed *****************')


    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info('***************** Verify Login test *****************')
        self.driver = setup # Initializing the chrome driver using setup fixture
        self.driver.get(self.baseURL) # Launching the base url
        self.obj=Login(self.driver) #creating object of LoginPage(PageObject) for accessing the action methods.If we create object of class, constructor will be automatically initialized
        self.obj.setUserName(self.username)
        self.obj.setPassword(self.password)
        self.obj.clickLogin()
        actual_title = self.driver.title
        expected_title = "Dashboard / nopCommerce administration"
        self.obj.clickLogout()
        assert actual_title == expected_title
        self.driver.close() # Closing the chrome driver
        self.logger.info('************ Login test is passed *****************')





