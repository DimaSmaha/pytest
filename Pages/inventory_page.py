from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class InventoryPage(BasePage):

    add_to_cart_btn = (By.ID, "add-to-cart-sauce-labs-backpack")
    remove_btn = (By.ID, "remove-sauce-labs-backpack")
    sauce_labs_backpack = (By.ID, "item_4_title_link")
    sauce_labs_backpack_title = (By.CLASS_NAME, "inventory_details_name large_size")

    def check_remove_btn_is_visible(self):
        self.is_visible(self.remove_btn)
