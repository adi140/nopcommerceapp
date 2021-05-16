class loginpage:

    textbox_email_id="Email"
    textbox_password_id="Password"
    button_click_xpath="/html/body/div[6]/div/div/div/div/div[2]/div[1]/div/form/div[3]/button"
    logout_linktext="Logout"

    def __init__(self,driver):
        self.driver=driver

    def setusername(self,username):
        self.driver.find_element_by_id(self.textbox_email_id).clear()
        self.driver.find_element_by_id(self.textbox_email_id).send_keys(username)

    def  setpassword(self,password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def loginbuttonclick(self):
        self.driver.find_element_by_xpath(self.button_click_xpath).click()

    def logoutbuttonclick(self):
        self.driver.find_element_by_link_text(self.logout_linktext).click()


