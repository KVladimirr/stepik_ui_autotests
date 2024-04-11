from test_lessons.pages.base_page import BasePage
from test_lessons.pages.locators import BasketPageLocators


class BasketPage(BasePage):

    def should_be_empty_basket(self):
        # Проверяем что нет товара
        assert self.is_not_element_present(*BasketPageLocators.FIRST_PRODUCT_IN_BASKET_NAME), \
            "There is a product in basket"

        # Проверяем что есть элемент пустой корзины
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_ELEMENT), "Empty basket element not found"

        # Проверяем что текст совпадает
        empty_basket_field = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_ELEMENT)
        empty_basket_field_text = empty_basket_field.text
        assert empty_basket_field_text == "Your basket is empty. Continue shopping", "Empty basket text is wrong"
