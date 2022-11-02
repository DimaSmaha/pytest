from Pages.LoginPage import LoginPage
from Config.config import TestData


class Test_Login():

    def test_login(self, driver):
        self.loginPage = LoginPage(driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData. PASSWORD)
        self.loginPage.get_url('inventory')