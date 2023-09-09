from pages.base_page import Page
from time import sleep

class MainPage(Page):

     def open_main(self):
         self.driver.get('https://www.amazon.com/')
         sleep(3)
         self.driver.refresh()

     def open_amazon_product_page(self):
         self.driver.get('https://www.amazon.com/gp/help/customer/display.html?nodeId=GX7NJQ4ZB8MHFRNJ')
         sleep(3)
         self.driver.refresh()