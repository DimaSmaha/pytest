from Pages.LoginPage import LoginPage
from Pages.inventoryPage import inventoryPage
from Config.config import TestData


class Test_Login():

    def test_login(self, driver):
        self.loginPage = LoginPage(driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage.get_url('inventory')

    def test_addToCartBtn(self, driver):
        self.loginPage = LoginPage(driver)
        self.inventoryPage = inventoryPage(driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage.get_url('inventory')
        self.inventoryPage.do_click(inventoryPage.addToCartBtn)
        self.inventoryPage.checkRemoveBtn()
        self.inventoryPage.do_click(inventoryPage.sauceLabsBackpack)
