from Pages.base_page import get_random_string
from Pages.redmine_register_page import RedmineRegisterPage
from Config.config import TestData

username: str = get_random_string()
password: str = "qwerty"
firstname: str = "Dima"
lastname: str = "Smaha"
email: str = get_random_string()+"@gmail.com"


class TestRedmineRegister:

    def test_register(self, driver):
        self.redmineRegister = RedmineRegisterPage(driver)
        self.redmineRegister.do_click(self.redmineRegister.register_btn)
        self.redmineRegister.check_url_contains('/account/register')
        self.redmineRegister.fill_register_input(username, password, firstname, lastname, email)
        self.redmineRegister.do_click(self.redmineRegister.confirm_register_btn)
        self.redmineRegister.is_visible(self.redmineRegister.success_register_notification)