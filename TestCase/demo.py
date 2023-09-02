import pytest
from UtilityScripts.excel_methods import ExcelMethods
from selenium import webdriver

sheet_name = 'demo'


class Testlogin:

    @pytest.mark.parametrize('s_num,count', ExcelMethods(sheet_name).get_parametrize_list())
    def test_1(self, s_num, count):
        if count != 22:
            status = True
        else:
            status = False
        ExcelMethods(sheet_name).update_result_in_excel(s_num, status)
        assert status
