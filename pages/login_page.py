from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" is self.url, "Login string is not url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_LINK), "Register button is not presented"
