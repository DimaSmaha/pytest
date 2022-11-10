from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class LoginPage(BasePage):

    username = (By.ID, "user-name")
    password = (By.ID, "password")
    login_button = (By.ID, "login-button")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)

    """PAGE ACTIONS"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.username,username)
        self.do_send_keys(self.password, password)
        self.do_click(self.login_button)
