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