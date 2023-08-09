from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

AMAZON_SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
AMAZON_SEARCH_BIN = (By.ID,"nav-search-submit-button")
@when('Input the product')
def Enter_Product_name(context):
    context.driver.find_element(*AMAZON_SEARCH_INPUT).send_keys('cell phone')
    context.driver.find_element(*AMAZON_SEARCH_BIN).click()
    sleep(2)


@then('Select one product')
def select_product(context):
    context.driver.find_element(By.CSS_SELECTOR,".a-section.aok-relative.s-image-fixed-height").click()
    sleep(2)

@then('Add it to the cart')
def add_to_cart(context):
    context.driver.find_element(By.ID,'add-to-cart-button').click()
    sleep(2)
    context.driver.find_element(By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]').click()
    context.driver.find_element(By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attach-sidesheet-view-cart-button-announce"]').click()
    #context.driver.find_element(By.CSS_SELECTOR,'[href="/cart?ref_=sw_gtc"]').click()
    sleep(2)


@then('Verify product in cart')
def no_product_in_cart(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'#sc-subtotal-label-buybox').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    sleep(2)
