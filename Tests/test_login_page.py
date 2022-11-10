from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Config.config import TestData


class TestLogin:

    def test_login(self, driver):
        self.loginPage = LoginPage(driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage.check_url_contains('inventory')

    def test_add_to_cart_btn(self, driver):
        self.loginPage = LoginPage(driver)
        self.inventoryPage = InventoryPage(driver)
        self.loginPage.do_login(TestData.USER_NAME, TestData.PASSWORD)
        self.loginPage.check_url_contains('inventory')
        self.inventoryPage.do_click(InventoryPage.addToCartBtn)
        self.inventoryPage.checkRemoveBtn()
        self.inventoryPage.do_click(InventoryPage.sauceLabsBackpack)
