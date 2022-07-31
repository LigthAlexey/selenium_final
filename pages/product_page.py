from .base_page import BasePage
from .locators import MainPageLocators
from .locators import SubmitPageLocators


class SubmitPage(BasePage):
    def go_to_submit_page(self):
        submit_link = self.browser.find_element(*MainPageLocators.SUBMIT_BUTTON)
        submit_link.click()

    def should_be_submit_link(self):
        assert self.is_element_present(*MainPageLocators.SUBMIT_BUTTON), "Submit button is not presented"

    def should_be_name(self):
        product_name = self.browser.find_element(*SubmitPageLocators.PRODUCT_NAME).text
        product_name_sale = self.browser.find_element(*SubmitPageLocators.PRODUCT_NAME_SALE).text
        assert product_name == product_name_sale, "Названия не соответствуют"

    def should_be_cost(self):
        product_cost = self.browser.find_element(*SubmitPageLocators.PRODUCT_COST).text
        product_cost_sale = self.browser.find_element(*SubmitPageLocators.PRODUCT_COST_SALE).text
        assert product_cost == product_cost_sale, "Цена не соответствуют"
