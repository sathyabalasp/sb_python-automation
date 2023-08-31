from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.sign_in_page import Sign_in_page
from pages.best_seller_page import Best_seller_page

class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.sign_in_page = Sign_in_page(driver)
        self.best_seller_page = Best_seller_page(driver)