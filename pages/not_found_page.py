# from selenium.webdriver.common.by import By
# from pages.base_page import Page
#
# class NotFoundPage(Page):
#
#     DOG_IMG = (By.CSS_SELECTOR,"img#d")
#
#     def store_original_window(self):
#         self.get_current_window()
#
#     def click_dog_img(self):
#         self.click(*self.DOG_IMG)
#
#     # def switch_to_new_window(self):
#     #     self.switch_to_new_windows()
from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class NotFoundPage(Page):
    DOG_IMG = (By.CSS_SELECTOR, 'img#d')


    def store_original_window(self):
        return self.get_current_window()

    def click_dog_img(self):
        self.click(*self.DOG_IMG)