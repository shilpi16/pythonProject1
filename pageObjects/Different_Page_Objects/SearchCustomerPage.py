import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

class SearchCustomer:
    #Add Customer Page
    txtEmail_xpath = "//*[@id='SearchEmail']"
    fname_xpath = "//*[@id='SearchFirstName']"
    lname_xpath = "//*[@id='SearchLastName']"
    search_btn_xpath = "//*[@id= 'search-customers']"
    search_table_xpath = "//*[@id= 'customers-grid_wrapper']"
    table_rows_xpath = "//*[@id= 'customers-grid']//tbody/tr"
    table_columns_xpath = "//*[@id= 'customers-grid']//tbody/tr/td"
    table_headers_xpath = "//table//tr//th"
    col_data_xpath = "//*[@id= 'customers-grid']//tbody/tr/td[$col_index]"

    def __init__(self,driver):
        self.driver=driver

    def setEmail(self,email):
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtEmail_xpath).send_keys(email)

    def set_fname(self, fname):
        self.driver.find_element(By.XPATH, self.fname_xpath).clear()
        self.driver.find_element(By.XPATH, self.fname_xpath).send_keys(fname)

    def set_lname(self, lname):
        self.driver.find_element(By.XPATH, self.lname_xpath).clear()
        self.driver.find_element(By.XPATH, self.lname_xpath).send_keys(lname)

    def clickSearch(self):
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()


    def getNoOfRows(self):
        return len(self.driver.find_element(By.XPATH, self.table_rows_xpath))

    def getNoOfColumns(self):
        return len(self.driver.find_element(By.XPATH, self.table_columns_xpath))

    def searchCustomerByEmail1(self, email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element_by_xpath(self.search_table_xpath)
            emailId=table.self.driver.find_element_by_xpath("//table[@id='customer-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if emailId == email:
                flag = True
                break
        return flag

    def get_column_index_by_col_name(self, column_name):
        columns = self.driver.find_elements(By.XPATH, self.table_headers_xpath)
        column_names = []
        i=1
        for column in columns:
            if column.text == column_name:
                return str(i)
            i = i +1
        raise Exception("colummn name not found")

    def searchCustomer_By_col_name(self, column_name, col_value):
        flag = False
        col_index = self.get_column_index_by_col_name(column_name)
        col_data_list = []
        col_xpath = self.col_data_xpath.replace("$col_index",str(col_index))
        column_cell_data = self.driver.find_elements(By.XPATH, col_xpath)
        for cell_data in column_cell_data:
            col_data_list.append(cell_data.text.strip())
        if col_value in col_data_list:
            flag = True
        return flag