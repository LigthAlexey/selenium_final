import pytest
from .pages.product_page import SubmitPage


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = SubmitPage(browser, link)
    page.open()
    page.should_be_submit_link()
    page.go_to_submit_page()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = SubmitPage(browser, link)
    page.open()
    page.should_be_submit_link()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = SubmitPage(browser, link)
    page.open()
    page.should_be_submit_link()
    page.go_to_submit_page()
    page.should_be_disappeared()

