from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_PAGE_CHECK = (By.XPATH, "//h1[@Class='a-spacing-small']")
    EMAIL_INPUT = (By.ID, 'ap_email')


    def verify_signing_in_page(self):
        self.verify_text('Sign in', *self.SIGN_IN_PAGE_CHECK)
        self.driver.find_element(*self.EMAIL_INPUT)
        self.verify_partial_url('ap/signin?openid')
