from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


TOP_MENU = (By.CSS_SELECTOR,'div.celwidget.c-f ul a')


@when('Click on BestSeller')
def open_best_seller(context):
    context.app.header.click_best_seller_btn()


@then('Verify this page has {number} top menu')
def link_count(context, number):
    context.app.best_seller_page.verify_top_menu_count(number)




@then('Verify each 5 top menus pages opens')
def verify_top_menu_page_opens(context):
    expected_text_top_menu = ['Amazon Best Sellers', 'Amazon Hot New Releases',
                              'Amazon Movers & Shakers', 'Amazon Most Wished For',
                              'Amazon Gift Ideas']
    actual_text_top_menu = []
    # top_menu_links = context.app.best_seller_page.bestseller_menu_links()
    top_menu_links = context.driver.find_elements(*TOP_MENU)
    for menu_link in top_menu_links[:]:
        menu_link.click()
        current_top_menu = context.app.best_seller_page.get_text_top_menu()
        actual_text_top_menu.append(current_top_menu)
        return top_menu_links
    assert actual_text_top_menu == expected_text_top_menu,\
        f'Expected {expected_text_top_menu} did not match actual {actual_text_top_menu}'



# @then('Verify each 5 top menus pages opens')
# def verify_top_menu_page_opens(context):
#     context.app.best_seller_page.verify_top_menu_page_opens()