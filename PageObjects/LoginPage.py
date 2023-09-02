class Login:
    def __init__(self, driver):
        self.driver = driver

        self.textbox_username_xpath = "//input[@id='txtUsername']"
        self.textbox_password_xpath = "//input[@id='txtPassword']"
        self.button_login_xpath = "//input[@id='btnLogin']"
        self.text_invalidmsg_xpath = "//span[@id='spanMessage']"


    def input_username(self,Username):
        self.driver.find_element_by_xpath(self.textbox_username_xpath).send_keys(Username)

    def input_password(self,Password):
        self.driver.find_element_by_xpath(self.textbox_password_xpath).send_keys(Password)

    def click_login(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def invalid_msg(self):
        return self.driver.find_element_by_xpath(self.text_invalidmsg_xpath).text