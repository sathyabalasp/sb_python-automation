from pages.main_page import MainPage
from pages.header import Header
from pages.search_result_page import SearchResultPage
from pages.sign_in_page import Sign_in_page
from pages.best_seller_page import Best_seller_page
from pages.term_and_condition_page import Term_And_Condition_Page
from pages.not_found_page import NotFoundPage
from pages.blog import Blog
class Application:

    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_result_page = SearchResultPage(driver)
        self.sign_in_page = Sign_in_page(driver)
        self.best_seller_page = Best_seller_page(driver)
        self.best_seller_page = Term_And_Condition_Page(driver)
        self.not_found_page = NotFoundPage(driver)
        self.blog = Blog(driver)