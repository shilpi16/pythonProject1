from selenium.webdriver.common.by import By

class Login():
    textbox_username_id = "Email"
    textbox_password_id = "Password"
    button_login_xpath = "//button[@type='submit']"
    link_logout_xpath = "//a[@href='/logout']"


# Initializing the driver by definning the constructor
# Contructor will automatically invoke at the time of object creation
# driver will come from actual testcase
# Here self.driver is the class variable

    def __init__(self,driver):
        self.driver=driver  #Assigning the driver coming from testcase to our local driver

#Implementing the action method for each locator

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click();

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click();




