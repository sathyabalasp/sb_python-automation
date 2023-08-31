from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
INPUT_SEARCH_ELEMENT = (By.ID,'twotabsearchtextbox')
SEARCH_ICON1 = (By.ID,'nav-search-submit-button')
ITEM_NAME = (By.XPATH,'//span[@class="a-color-state a-text-bold"]')

@when('Search for {item_name}')
def input_search_product(context,item_name):
   # context.driver.find_element(*INPUT_SEARCH_ELEMENT).send_keys(item_name)
   # context.driver.find_element(*SEARCH_ICON1).click()
   context.app.header.search_product(item_name)

@then('Verify search {expected_text} is correct')
def verify_search(context,expected_text):
    # name_item = context.driver.find_element(*ITEM_NAME).text
    # assert expected_text == name_item, f'Error, expected {expected_text} did not match actual {name_item}'
    context.app.search_result_page.verify_search_result(expected_text)