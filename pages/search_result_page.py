from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultPage(Page):
     SEARCH_RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
     SIGN_IN_PAGE_CHECK = (By.XPATH, "//h1[@Class='a-spacing-small']")
     def verify_search_result(self, expected_text):
         actual_text = self.find_element(*self.SEARCH_RESULT).text
         assert actual_text == expected_text,  \
             f'Error, expected {expected_text} did not match actual {actual_text}'


     # def Verify_signing_in_page(self,text):
     #     actual_text1 = self.input_text(*self.SIGN_IN_PAGE_CHECK)
     #     assert actual_text1 == text, \
     #         f'Error, expected {text} did not match actual {actual_text1}'