from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class inventoryPage(BasePage):

    addToCartBtn = (By.ID, "add-to-cart-sauce-labs-backpack")
    removeBtn = (By.ID, "remove-sauce-labs-backpack")
    sauceLabsBackpack = (By.ID, "item_4_title_link")
    sauceLabsBackpackTitle = (By.CLASS_NAME, "inventory_details_name large_size")

    def checkRemoveBtn(self):
        self.is_visible(self.removeBtn)
