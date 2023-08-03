from behave import given, when, then
from selenium.webdriver.common.by import By


@given('Open Amazon page')
def open_amazon(context):
    context.driver.get('https://www.amazon.com/')


@when('Click Returns and Orders')
def return_orders(context):
    context.driver.find_element(By.ID,'nav-orders').click()


@then('Verify sign in page opened')
def sign_in_page(context):
    expected_result = 'Sign in'
    actual_result = context.driver.find_element(By.XPATH,"//h1[@Class='a-spacing-small']").text
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'


@then('Verify Email input field is present')
def email_input_field(context):
    expected_result = context.driver.find_element(By.XPATH, "// input[@type = 'email']").is_displayed()
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#ap_email").is_displayed()
    assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'

