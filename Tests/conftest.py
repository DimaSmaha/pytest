import pytest
from selenium import webdriver
from Config.config import TestData


# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

# @pytest.fixture(params=["chrome"], scope='class')
# def init_driver(request):
#     print("################ ", request.param)
#     if request.param == "chrome":
#         web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
#     request.cls.driver = web_driver
#     yield
#     web_driver.close()

# this file is a config for tests and its generates driver
# in other case u should put driver to BasePage
@pytest.fixture()
def driver():
    driver = webdriver.Chrome(executable_path=TestData.chrome_executable_path)
    driver.maximize_window()
    yield driver
    driver.quit()
