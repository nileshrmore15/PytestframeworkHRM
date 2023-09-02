class EmpStatus:
    def __init__(self,driver):
        self.driver = driver

        self.button_add_status_xpath = "//input[@id='btnAdd']"
        self.inputfield_name_xpath = "//input[@id='empStatus_name']"
        self.total_field_xpath = "//tbody/tr"
        self.button_save_xpath = "//input[@id='btnSave']"

    def click_addbutton(self):
        self.driver.find_element_by_xpath(self.button_add_status_xpath).click()

    def input_new_status(self,Name):
        self.driver.find_element_by_xpath(self.inputfield_name_xpath).send_keys(Name)

    def total_status(self):
        return self.driver.find_elements_by_xpath(self.total_field_xpath)

    def click_savebutton(self):
        self.driver.find_element_by_xpath(self.button_save_xpath).click()