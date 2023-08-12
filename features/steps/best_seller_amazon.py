from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

BEST_SELLER_PAGE = (By.CSS_SELECTOR,'a[href="/gp/bestsellers/?ref_=nav_cs_bestsellers"]')
LINK_AMOUNT = (By.CSS_SELECTOR,'._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR')
@when('Click on BestSeller')
def open_best_seller(context):
    context.driver.find_element(*BEST_SELLER_PAGE).click()

@then('Verify this page has {number} Links')
def link_count(context,number):
    number = int(number)
    links_no = context.driver.find_elements(*LINK_AMOUNT)
    assert len(links_no) == number , f'Expected {number} links but got {len(links_no)}'


