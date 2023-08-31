from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
     SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
     EMPTY_CART_TEXT = (By.CSS_SELECTOR, '.a-row.sc-your-amazon-cart-is-empty')
     ADD_TO_CART = (By.ID, 'add-to-cart-button')
     NO_THANKS = (By.CSS_SELECTOR, '.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]')
     GOTO_CART_PAGE = (By.CSS_SELECTOR, '[href="/cart?ref_=sw_gtc"]')
     SUBTOTAL_TEXT = (By.CSS_SELECTOR, '#sc-subtotal-label-buybox')
     def verify_search_result(self, result):
         self.verify_text(result, *self.SEARCH_RESULT)


     def verifying_cart_is_empty(self, text):
         self.verify_text(text,*self.EMPTY_CART_TEXT)


     def verify_number_of_items_in_cart(self,text):
        self.verify_text(text,*self.SUBTOTAL_TEXT)

     def add_product_to_cart(self):
         self.click(*self.ADD_TO_CART)
         self.click(*self.NO_THANKS)
         self.click(*self.GOTO_CART_PAGE)
