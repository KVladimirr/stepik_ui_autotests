from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_MAIL_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, '[href="/en-gb/password-reset/"]')
    LOGIN_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="login_submit"]')

    REGISTRATION_EMAIL_INPUT = (By.CSS_SELECTOR, '#id_registration-email')
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_REPEAT_PASSWORD_INPUT = (By.CSS_SELECTOR, '#id_registration-password2')
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, '[name="registration_submit"]')


class ProductPageLocators:
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.col-sm-6.product_main .price_color')
    MESSAGE_WITH_CART_PRICE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in')
    CART_PRICE = (By.CSS_SELECTOR, '.alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner p:first-child strong')
    MESSAGE_WITH_PRODUCT_IN_CART = (By.CSS_SELECTOR, '#messages div:first-child div strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
