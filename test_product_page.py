from .pages.product_page import SubmitPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = SubmitPage(browser, link)
    page.open()
    page.should_be_submit_link()
    page.go_to_submit_page()
    page.solve_quiz_and_get_code()
    page.should_be_name()
    page.should_be_cost()