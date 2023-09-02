import pytest
from selenium import webdriver
driver = None
import configparser
config = configparser.ConfigParser()
config.read("Utilities/input.properties")

@pytest.fixture
def setup(request):
    global driver
    request.cls.driver = webdriver.Chrome() #(executable_path="D://pariplay//SELENIUM_PYTEST_UI_FRAMEWORK-master//SELENIUM_PYTEST_UI_FRAMEWORK-master//Driver//chromedriver.exe")
    request.cls.driver.get('https://opensource-demo.orangehrmlive.com')
    yield
    request.cls.driver.quit()


