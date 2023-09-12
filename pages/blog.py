from pages.base_page import Page

class Blog(Page):
    def verify_opened(self):
        self.verify_partial_url('www.aboutamazon.com')


    # def close_blog(self):
    #     self.close_page()
    #
    #
    # def return_to_original_window(self, window_id):
    #     self.switch_to_window(window_id)
