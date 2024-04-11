import time

import pytest

from test_lessons.pages.main_page import MainPage
from test_lessons.pages.login_page import LoginPage
from test_lessons.pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


@pytest.mark.skip
@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_login_page(self, browser):
        login_page = LoginPage(browser, login_link)
        login_page.open()
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()

    page.should_be_basket_button()
    page.go_to_basket_page()

    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_empty_basket()
