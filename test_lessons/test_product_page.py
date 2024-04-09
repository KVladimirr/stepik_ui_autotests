import time

from .pages.product_page import ProductPage

product_page_link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, product_page_link)
    page.open()

    page.check_query_param()

    page.add_to_cart()
    page.solve_quiz_and_get_code()

    page.should_be_message_with_cart_price()
    page.should_be_message_with_product_in_cart()

    page.basket_price_equals_product()
    page.product_name_is_same_in_message()
