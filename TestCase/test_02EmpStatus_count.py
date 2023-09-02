import time
import pytest
from PageObjects.DashboardPage import dashboard
from PageObjects.LoginPage import Login
from selenium.webdriver import ActionChains
from PageObjects.EmploymentStatusPage import EmpStatus
from Utilities.logger import logclass
from Utilities.random_status import status_generator
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.mark.usefixtures("setup")
class TestAddButton(logclass):
    def test_001(self):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard(self.driver)
        es = EmpStatus(self.driver)
        log.info("TEST CASE 001, To test the add button in employment status page")
        log.info("test started")
        lg.input_username(config.get("credential","correct_username"))
        lg.input_password(config.get("credential","correct_password"))
        lg.click_login()
        log.info("login successful")
        ActionChains(self.driver).move_to_element(db.hover_admin()).perform()
        log.info("hover on Admin")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(db.hover_job()).perform()
        log.info("hover on Job")
        ActionChains(self.driver).move_to_element(db.hover_emp_status()).click().perform()
        log.info("hover and click on Employment Status")
        Old_Status_count = 0
        for i in es.total_status():
            Old_Status_count = Old_Status_count + 1
        log.info("old status count saved")
        es.click_addbutton()
        log.info("clicked on add button")
        es.input_new_status(status_generator())
        log.info("added new status")
        es.click_savebutton()
        log.info("clicked on save button")
        time.sleep(4)
        New_Status_count = 0
        for j in es.total_status():
            New_Status_count = New_Status_count + 1
        log.info("new status count saved")
        if Old_Status_count + 1 == New_Status_count:
            assert True
            log.info("Test case passed, Add functionality is workng fine")
        else:
            self.driver.save_screenshot('Screenshots\\Addbutton_001.png')
            log.error("Test case failed")
            assert False