from test_lessons.pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()

    def check_query_param(self):
        assert '?promo=newYear' in self.browser.current_url

    def basket_price_equals_product(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_value = product_price.text[1:]

        basket_price = self.browser.find_element(*ProductPageLocators.CART_PRICE)
        basket_price_value = basket_price.text[1:]

        assert float(product_price_value) == float(basket_price_value), "Basket price do not equals product"

    def should_be_message_with_cart_price(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_CART_PRICE), "No message with cart price"

    def should_be_message_with_product_in_cart(self):
        assert self.is_element_present(*ProductPageLocators.MESSAGE_WITH_PRODUCT_IN_CART)

    def product_name_is_same_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        product_name_text = product_name.text

        product_message = self.browser.find_element(*ProductPageLocators.MESSAGE_WITH_PRODUCT_IN_CART)
        product_message_text = product_message.text

        assert product_name_text == product_message_text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_WITH_PRODUCT_IN_CART), \
            "Success message is presented, but should not be"

    def element_should_disappear(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_WITH_PRODUCT_IN_CART, timeout=4), \
            "Element does not disappear"
