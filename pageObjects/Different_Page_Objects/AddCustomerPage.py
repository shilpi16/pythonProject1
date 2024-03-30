import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class AddCustomer:
    lnk_customer_menu_xpath = "//a[@href='#']//p[contains(text(), 'Customers')]"
    lnl_customer_sub_menu_xpath = "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    btn_add_new_customer_xpath = "//a[@href='/Admin/Customer/Create']"
    tb_email_detail_xpath = "//*[@id='Email']"
    tb_password_detail_xpath = "//*[@id='Password']"
    tb_fname_detail_xpath = "//*[@id='FirstName']"
    tb_lname_detail_xpath = "//*[@id='LastName']"
    rb_male_xpath = "//*[@id='Gender_Male']"
    rb_female_xpath = "//input[@id='Gender_Female']"
    tb_dob_xpath = "//*[@id='DateOfBirth']"
    calender_dob_xpath = "//span[contains(@class, 'datepicker')]//span[@aria-label='select']"
    tb_company_xpath = "//*[@id='Company']"
    cb_tax_exempt_xpath = "//*[@id='IsTaxExempt']"
    tb_news_letter = "//*[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    #list_customer_roles_xpath = "//*[@id='SelectedCustomerRoleIds_listbox']"
    list_customer_roles_xpath = "//*[contains(@class,'input-group-required')]"
    customer_role_as_guests = "//li[contains(text(),'Guests')]"
    customer_role_as_administrators = "//li[contains(text(),'Administrators')]"
    customer_role_as_moderator = "//li[contains(text(),'Forum Moderators')]"
    customer_role_as_registered = "//li[contains(text(),'Registered')]"
    customer_role_as_vendors = "//li[contains(text(),'Vendors')]"
    delete_registered_role = "//ul[@id='SelectedCustomerRoleIds_taglist']//li//span[@title='delete']"
    customer_roles_options = "//*[@id='SelectedCustomerRoleIds_listbox']//li"
    drp_manage_vendor = "//*[@id='VendorId']"
    cb_active_xpath = "//*[@id='Active']"
    ta_admin_comment_xpath = "//*[@id='AdminComment']"
    btn_save_xpath = "//*[@name='save']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element(By.XPATH, self.lnk_customer_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH, self.lnl_customer_sub_menu_xpath).click()

    def clickOnAddnew(self):
        self.driver.find_element(By.XPATH, self.btn_add_new_customer_xpath).click()

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.tb_email_detail_xpath).send_keys(email)

    def setPassword(self, password):
        self.driver.find_element(By.XPATH, self.tb_password_detail_xpath).send_keys(password)

    def setFname(self, fname):
        self.driver.find_element(By.XPATH, self.tb_fname_detail_xpath).send_keys(fname)

    def setLname(self, lname):
        self.driver.find_element(By.XPATH, self.tb_lname_detail_xpath).send_keys(lname)

    def setDOB(self, dob):
        self.driver.find_element(By.XPATH, self.tb_dob_xpath).send_keys(dob)

    def setCompanyName(self, comp_name):
        self.driver.find_element(By.XPATH, self.tb_company_xpath).send_keys(comp_name)

    def selectVendor(self, text):
        drp=Select(self.driver.find_element(By.XPATH, self.drp_manage_vendor))
        drp.select_by_visible_text(text)

    def setGender(self, gender):
        if gender=='Male':
            self.driver.find_element(By.XPATH, self.rb_male_xpath).click()
        elif gender=='Female':
            self.driver.find_element(By.XPATH, self.rb_female_xpath).click()
        else:
            self.driver.find_element(By.XPATH, self.rb_male_xpath).click()

    def setAdminContent(self, content):
        self.driver.find_element(By.XPATH, self.ta_admin_comment_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element(By.XPATH, self.btn_save_xpath).click()


    def setCustomerRoles(self,role):
        #self.driver.find_element(By.XPATH, self.delete_registered_role).click()
        self.driver.find_element(By.XPATH, self.list_customer_roles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_as_registered)
        elif role == 'Administrators':
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_as_administrators)
        elif role == 'Guests':
            # Here user can be registered user or guest user, only one
            time.sleep(3)
            self.driver.find_element(By.XPATH, self.delete_registered_role).click()
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_as_guests)
        elif role == 'Vendors':
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_as_vendors)
        else:
            self.driver.find_element(By.XPATH, self.delete_registered_role).click()
            self.listitem = self.driver.find_element(By.XPATH, self.customer_role_as_guests)
        time.sleep(3)
        #Sometime if click is not working in some of the elements use execute_script() methods
        self.driver.execute_script("arguments[0].click();", self.listitem);

    def setCustomerRoles1(self,role):    #Alternate method of selecting customer roles
        self.driver.find_element(By.XPATH, self.delete_registered_role).click()
        self.driver.find_element(By.XPATH, self.list_customer_roles_xpath).click()
        options = self.driver.find_elements(By.XPATH, self.customer_roles_options)
        for option in options:
            print(option.text)
            if option.text==role:
               option.click();
               break;

