from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.browser.current_url, "login is not in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_MAIL_INPUT), "No login mail input"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), "No login password input"
        assert self.is_element_present(*LoginPageLocators.LOGIN_SUBMIT_BUTTON), "No login submit button"
        assert self.is_element_present(*LoginPageLocators.FORGOT_PASSWORD_BUTTON), "No login forgot password button"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL_INPUT), "No registration mail input"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT), "No registration password input"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_REPEAT_PASSWORD_INPUT), "No reg rep pass input"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON), "No registration submit button"