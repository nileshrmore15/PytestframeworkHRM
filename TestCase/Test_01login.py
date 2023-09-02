import time
import pytest
from PageObjects.LoginPage import Login
from PageObjects.DashboardPage import dashboard
from Utilities.logger import logclass
from UtilityScripts.excel_methods import ExcelMethods
sheet_name = "test_login"
@pytest.mark.usefixtures("setup")
class Testlogin(logclass):

    @pytest.mark.parametrize("s_num,username,password,condition", ExcelMethods("test_login").get_parametrize_list())
    def test_001(self, s_num, username, password, condition):
        log = self.getthelogs()
        lg = Login(self.driver)
        db = dashboard(self.driver)
        log.info("TEST CASE 001, to test the login functionality with correct credential")
        log.info("test started")
        lg.input_username(username)
        log.info("entered username")
        lg.input_password(password)
        log.info("entered password")
        lg.click_login()
        log.info("clicked login")
        time.sleep(2)
        if condition == '+':
            if 'Welcome' in db.welcome_msg():
                log.info("Test Case Pass")
                status = True
            else:
                self.driver.save_screenshot('Screenshots\\Testlogin_001.png')
                log.critical("Test Case Failed")
                status = False
        elif condition == '-':
            if 'Invalid credentials' in lg.invalid_msg():
                status = True
                log.info("Test Case Pass")
            else:
                self.driver.save_screenshot('Screenshots\\Testlogin_002.png')
                log.critical("Test Case Failed")
                status = False
        ExcelMethods(sheet_name).update_result_in_excel(s_num, status)
        assert status
