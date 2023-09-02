class dashboard:
    def __init__(self, driver):
        self.driver = driver

        self.text_welcomemsg_xpath = "//a[@id='welcome']"
        self.button_admin_xpath = "//a[@id='menu_admin_viewAdminModule']"
        self.button_job_xpath = "//a[@id='menu_admin_Job']"
        self.button_employment_status_xpath = "//a[@id='menu_admin_employmentStatus']"

    def welcome_msg(self):
        return self.driver.find_element_by_xpath(self.text_welcomemsg_xpath).text

    def hover_admin(self):
        return self.driver.find_element_by_xpath(self.button_admin_xpath)

    def hover_job(self):
        return self.driver.find_element_by_xpath(self.button_job_xpath)

    def hover_emp_status(self):
        return self.driver.find_element_by_xpath(self.button_employment_status_xpath)