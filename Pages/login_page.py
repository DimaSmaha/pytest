from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class LoginPage(BasePage):

    Username = (By.ID, "user-name")
    Password = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")

    """constructor of the page class"""
    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    """PAGE ACTIONS"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.do_send_keys(self.Username,username)
        self.do_send_keys(self.Password, password)
        self.do_click(self.LOGIN_BUTTON)
