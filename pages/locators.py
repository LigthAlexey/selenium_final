from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')
    LOGIN_LINK = (By.CSS_SELECTOR, '[name="login_submit"]')
