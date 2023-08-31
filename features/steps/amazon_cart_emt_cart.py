from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep


# GOTO_CART_ICON = (By.CSS_SELECTOR,'a[href="/gp/cart/view.html?ref_=nav_cart"]')
# EMPTY_CART_TEXT = (By.CSS_SELECTOR,'.a-row.sc-your-amazon-cart-is-empty')
@when('clicks on the cart icon')
def cart_icon_click(context):
    # context.driver.find_element(*GOTO_CART_ICON).click()
    context.app.header.click_cart_icon()
    sleep(4)

@then('Verify {text} text present')
def check_cart(context,text):
    # expected_result = 'Your Amazon Cart is empty'
    # actual_result = context.driver.find_element(*EMPTY_CART_TEXT).text
    # assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
    # context.app.search_result_page.verify_cart_is_empty()
    context.app.search_result_page.verifying_cart_is_empty(text)
