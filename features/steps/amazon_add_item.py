from behave import given, when, then
from selenium.webdriver.common.by import By
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

AMAZON_SEARCH_INPUT = (By.CSS_SELECTOR, '#twotabsearchtextbox')
AMAZON_SEARCH_BIN = (By.ID,'nav-search-submit-button')
SELECT_PRODUCT = (By.CSS_SELECTOR,".a-section.aok-relative.s-image-fixed-height")
ADD_TO_CART = (By.CSS_SELECTOR,'#add-to-cart-button')
ADD_TO_CART1 =(By.CSS_SELECTOR,'#mbc-buybutton-addtocart-1-announce')
CART_INPUT_BOX = (By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attach-sidesheet-view-cart-button-announce"]')
NO_THANKS = (By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attachSiNoCoverage-announce"]')
GOTO_CART_PAGE1 = (By.CSS_SELECTOR,'.a-button-input[aria-labelledby="attach-sidesheet-view-cart-button-announce"]')
GOTO_CART_PAGE2 = (By.CSS_SELECTOR,'[href="/cart?ref_=sw_gtc"]')
#GOTO_CART_PAGE3 = (By.CSS_SELECTOR,'#mbc-offer-view-cart-1')
SUBTOTAL_TEXT = (By.CSS_SELECTOR,'#sc-subtotal-label-buybox')


@when('Input the product')
def Enter_Product_name(context):
    context.driver.find_element(*AMAZON_SEARCH_INPUT).send_keys('cell phone')
    context.driver.find_element(*AMAZON_SEARCH_BIN).click()



@then('Select one product')
def select_product(context):
    context.driver.find_element(*SELECT_PRODUCT).click()



@then('Add it to the cart')
def adding_to_cart(context):
   context.driver.wait.until(EC.element_to_be_clickable(ADD_TO_CART)).click()
    #context.driver.find_element(*ADD_TO_CART).click()

    context.driver.wait.until(EC.element_to_be_clickable(CART_INPUT_BOX),message='Cart Input btn not clickable').click()
    context.driver.find_element(*NO_THANKS).click()
    #context.driver.wait.until(EC.element_to_be_clickable(GOTO_CART_PAGE2)).click()
    #context.driver.find_element(*GOTO_CART_PAGE3).click()
    context.driver.find_element(*GOTO_CART_PAGE2).click()



@then('Verify product in cart')
def no_product_in_cart(context):
    expected_result = 'Subtotal (1 item):'
    actual_result = context.driver.find_element(*SUBTOTAL_TEXT).text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

