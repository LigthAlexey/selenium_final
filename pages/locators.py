from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket")  # "button[value='Добавить в корзину']")
    NOT_ELEMENT = (By.CSS_SELECTOR, '#messages strong')
    IS_DISAPPEARED = (By.CSS_SELECTOR, '#messages strong')


class LoginPageLocators():
    REGISTER_LINK = (By.CSS_SELECTOR, '[name="registration_submit"]')
    LOGIN_LINK = (By.CSS_SELECTOR, '[name="login_submit"]')


class SubmitPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_NAME_SALE = (By.CSS_SELECTOR, '#messages strong')
    PRODUCT_COST_SALE = (By.CSS_SELECTOR, 'div.alertinner p strong')
    PRODUCT_COST = (By.CSS_SELECTOR, 'div.col-sm-6.product_main p.price_color')
