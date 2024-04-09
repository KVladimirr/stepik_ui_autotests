import time
from test_lessons.pages.main_page import MainPage
from test_lessons.pages.login_page import LoginPage

link = "http://selenium1py.pythonanywhere.com/"
login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_login_page(browser):
    login_page = LoginPage(browser, login_link)
    login_page.open()
    login_page.should_be_login_page()
