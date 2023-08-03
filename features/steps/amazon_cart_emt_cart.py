from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep

@when('clicks on the cart icon')
def cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR,'a[href="/gp/cart/view.html?ref_=nav_cart"]').click()
    sleep(4)

@then('Verify Cart is empty')
def check_cart(context):
    expected_result = 'Your Amazon Cart is empty'
    actual_result = context.driver.find_element(By.CSS_SELECTOR,'.a-row.sc-your-amazon-cart-is-empty').text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
