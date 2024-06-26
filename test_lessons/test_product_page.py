import time
import pytest

from .pages.product_page import ProductPage
from test_lessons.pages.basket_page import BasketPage
from test_lessons.pages.login_page import LoginPage

product_page_link = " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


@pytest.mark.need_review
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work"
                                               "_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()

    # page.check_query_param()
    page.should_not_be_success_message()

    page.add_to_cart()
    page.solve_quiz_and_get_code()

    page.should_be_message_with_cart_price()
    page.should_be_message_with_product_in_cart()

    page.basket_price_equals_product()
    page.product_name_is_same_in_message()

    # page.element_should_disappear()


@pytest.mark.xfail(reeason="Fail test")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_link)
    page.open()

    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, product_page_link)
    page.open()

    page.should_not_be_success_message()


@pytest.mark.xfail(reeason="Fail test")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, product_page_link)
    page.open()

    page.add_to_cart()
    page.element_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, product_page_link)
    page.open()

    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()


class TestUserAddToBasketFromProductPage:

    @pytest.fixture
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        password = "q1w2e3r4t5y6u7"

        page = ProductPage(browser, product_page_link)
        page.open()

        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)

        login_page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser, setup):
        page = ProductPage(browser, product_page_link)
        page.open()

        page.should_not_be_success_message()
        time.sleep(5)

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser, setup):
        page = ProductPage(browser, product_page_link)
        page.open()

        # page.check_query_param()
        page.should_not_be_success_message()

        page.add_to_cart()
        # page.solve_quiz_and_get_code()

        page.should_be_message_with_cart_price()
        page.should_be_message_with_product_in_cart()

        page.basket_price_equals_product()
        page.product_name_is_same_in_message()

        time.sleep(5)

        # page.element_should_disappear()
