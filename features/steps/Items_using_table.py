from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
INPUT_SEARCH_ELEMENT = (By.ID,'twotabsearchtextbox')
SEARCH_ICON1 = (By.ID,'nav-search-submit-button')
ITEM_NAME = (By.XPATH,'//span[@class="a-color-state a-text-bold"]')

@when('Search for {item_name}')
def input_search_product(context,item_name):
    context.app.header.search_product(item_name)

@then('Verify search {expected_text} is correct')
def verify_search(context,expected_text):
    context.app.search_result_page.verify_search_result(expected_text)