import string

from selenium.webdriver.common.by import By

from Config.config import TestData
from Pages.base_page import BasePage


class RedmineRegisterPage(BasePage):

    register_btn = (By.CLASS_NAME, "register")
    username_input = (By.ID, "user_login")
    password_input = (By.ID, "user_password")
    confirm_password_input = (By.ID, "user_password_confirmation")
    firstname_input = (By.ID, "user_firstname")
    lastname_input = (By.ID, "user_lastname")
    email_input = (By.ID, "user_mail")
    confirm_register_btn = (By.NAME, "commit")
    success_register_notification = (By.ID, "flash_notice")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url1)

    def fill_register_input(self, username: string, password: string,
                            firstname: string, lastname: string, email: string):
        self.do_send_keys(self.username_input, username)
        self.do_send_keys(self.password_input, password)
        self.do_send_keys(self.confirm_password_input, password)
        self.do_send_keys(self.firstname_input, firstname)
        self.do_send_keys(self.lastname_input, lastname)
        self.do_send_keys(self.email_input, email)
