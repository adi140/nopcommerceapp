import time
from selenium.webdriver.support.ui import Select

class addcustomer:

    linkcustomer_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a"
    #linkcustomer_xpath="//a[@href='#']//p[contains(text(),'Customers')]"
    linkcustomermenuitem_xpath="/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/ul/li[1]/a/p"
    #linkcustomermenuitem_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
    addnewcustomer_xpath="/html/body/div[3]/div[1]/form[1]/div/div/a"
    emailid_id="Email"
    password_id="Password"
    FirstName_id="//input[@name='FirstName']"
    LastName_id="LastName"
    MaleRadioButton_xpath="//*[@id='Gender_Male']"
    FemaleRadioButton_xpath="//*[@id='Gender_Female']"
    FindCalendar_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[6]/div[2]/span[1]/span/span/span"
    clickondate_bytext="//a[text()='28']"
    CompanyName_id="Company"
    IsTextExempt_id="IsTaxExempt"
    Newsletter_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[9]/div[2]/div/div[1]/div/div"
    Customerrole_xpath="/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[10]/div[2]/div/div[1]/div/div"
    #Customerrole_xpath="//div[@class='k-multiselect-wrap k-floatwrap']"
    lstitemAdministrators_xpath = "//li[contains(text(),'Administrators')]"
    listcontainforcustomerrole_xpath="//li[contains(text(),'Registered')]"
    ManageVendor_xpath="//*[@id='VendorId']"
    Active_id="Active"
    AdminComment_xpath="//*[@id='AdminComment']"
    #SaveButton_xpath="//button[@name='Save']"
    SaveButton_xpath="/html/body/div[3]/div[1]/form/div[1]/div/button[1]"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomersMenu(self):
        self.driver.find_element_by_xpath(self.linkcustomer_xpath).click()
    #time.sleep(5)
    def clickOnCustomersMenuItem(self):
        #self.driver.find_element_by_xpath(self.linkcustomermenuitem_xpath).click()
        self.driver.execute_script("arguments[0].click();", self.driver.find_element_by_xpath(self.linkcustomermenuitem_xpath))
    #time.sleep(5)

    def clickOnAddnew(self):
        self.driver.find_element_by_xpath(self.addnewcustomer_xpath).click()
    #time.sleep(5)

    def setEmail(self, email):
        self.driver.find_element_by_id(self.emailid_id).send_keys(email)
    #time.sleep(5)

    def setPassword(self, password):
        self.driver.find_element_by_id(self.password_id).send_keys(password)
    #time.sleep(5)

    def setCustomerRoles(self, role):
        self.driver.find_element_by_xpath(self.Customerrole_xpath).click()
        time.sleep(3)
        if role == 'Administrator':
            self.listitem = self.driver.find_element_by_xpath(self.lstitemAdministrators_xpath)
            self.driver.execute_script("arguments[0].click();", self.listitem)
    #time.sleep(5)

    def setManagerOfVendor(self, value):
        drp = Select(self.driver.find_element_by_xpath(self.ManageVendor_xpath))
        drp.select_by_visible_text(value)
    #time.sleep(5)

    def setGender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_xpath(self.MaleRadioButton_xpath).click()
        elif gender == 'Female':
            self.driver.find_element_by_xpath(self.FemaleRadioButton_xpath).click()
        else:
            self.driver.find_element_by_xpath(self.MaleRadioButton_xpath).click()
    #time.sleep(5)

    def setFirstName(self, fname):
        self.driver.find_element_by_xpath(self.FirstName_id).send_keys(fname)
    #time.sleep(5)

    def setLastName(self, lname):
        self.driver.find_element_by_id(self.LastName_id).send_keys(lname)
    time.sleep(5)
    #def setDob(self, dob):
    #    self.driver.find_element_by_xpath(self.txtDob_xpath).send_keys(dob)

    def dob(self):
        self.driver.find_element_by_xpath("/html/body/div[3]/div[1]/form/section/div/div/nop-cards/nop-card/div/div[2]/div[6]/div[2]/span[1]/span/span").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_xpath("//a[text()='19']").click()
    #time.sleep(5)

    def setCompanyName(self, comname):
        self.driver.find_element_by_id(self.CompanyName_id).send_keys(comname)
    #time.sleep(5)

    def setAdminContent(self, content):
        self.driver.find_element_by_xpath(self.AdminComment_xpath).send_keys(content)
    #time.sleep(5)

    def clickOnSave(self):
        self.driver.find_element_by_xpath(self.SaveButton_xpath).click()
