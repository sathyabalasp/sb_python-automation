from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

AMAZON_SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
AMAZON_SEARCH_BIN = (By.ID,"nav-search-submit-button")
SELECT_PRODUCT = (By.CSS_SELECTOR,".a-section.aok-relative.s-image-fixed-height")
ADD_TO_CART = (By.ID,'add-to-cart-button')
NO_THANKS = (By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]')
GOTO_CART_PAGE1 = (By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attach-sidesheet-view-cart-button-announce"]')
GOTO_CART_PAGE2 = (By.CSS_SELECTOR,'[href="/cart?ref_=sw_gtc"]')
SUBTOTAL_TEXT = (By.CSS_SELECTOR,'#sc-subtotal-label-buybox')

@when('Input the product')
def Enter_Product_name(context):
    context.driver.find_element(*AMAZON_SEARCH_INPUT).send_keys('cell phone')
    context.driver.find_element(*AMAZON_SEARCH_BIN).click()
    sleep(2)


@then('Select one product')
def select_product(context):
    context.driver.find_element(*SELECT_PRODUCT).click()
    sleep(2)

@then('Add it to the cart')
def add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART).click()
    sleep(2)
    context.driver.find_element(*NO_THANKS).click()
    #context.driver.find_element(*GOTO_CART_PAGE1).click()
    context.driver.find_element(*GOTO_CART_PAGE2).click()
    sleep(2)


@then('Verify product in cart')
def no_product_in_cart(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(*SUBTOTAL_TEXT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    sleep(2)
