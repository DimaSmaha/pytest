from Pages.login_page import LoginPage
from Pages.inventory_page import InventoryPage
from Config.config import TestData


class TestLogin:

    def test_login(self, driver):
        self.loginPage = LoginPage(driver)
        self.loginPage.do_login(TestData.user_name, TestData.password)
        self.loginPage.check_url_contains('inventory')

    def test_add_to_cart_btn(self, driver):
        self.loginPage = LoginPage(driver)
        self.inventoryPage = InventoryPage(driver)
        self.loginPage.do_login(TestData.user_name, TestData.password)
        self.loginPage.check_url_contains('inventory')
        self.inventoryPage.do_click(InventoryPage.add_to_cart_btn)
        self.inventoryPage.check_remove_btn_is_visible()
        self.inventoryPage.do_click(InventoryPage.sauce_labs_backpack)
