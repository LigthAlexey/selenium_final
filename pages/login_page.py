from .base_page import BasePage
from .locators import LoginPageLocators

# Для проверки нажатия кнопки регистрации если нужно, по условию задания нет...
'''from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException'''


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.url, "Login string is not url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), "Login button is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"

    def register_new_user(self, email, password):
        assert self.is_element_present(*LoginPageLocators.EMAIL_STR), "Поле почты не найдено"
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_STR)
        email_field.send_keys(email)
        assert self.is_element_present(*LoginPageLocators.PASS_STR), "Поле пароля не найдено"
        pass_field = self.browser.find_element(*LoginPageLocators.PASS_STR)
        pass_field.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.PASS_STR_RTR), "Поле пароля2 не найдено"
        pass_field_rtr = self.browser.find_element(*LoginPageLocators.PASS_STR_RTR)
        pass_field_rtr.send_keys(password)
        assert self.is_element_present(*LoginPageLocators.REGISTER_BUTTON), "Register button is not presented"
        button_pass = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        button_pass.click()

        # Для проверки если нужно, по условию задания нет...
        '''try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '[name="registration_submit"]'))).click()
        except TimeoutException as e:
            print("Element click failed")'''
