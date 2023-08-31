from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
@given('Open Amazon page')
def open_amazon(context):
    context.app.main_page.open_main()

@when('Click Returns and Orders')
def return_orders(context):
    context.app.header.returns_and_orders()

@when('Click on button from SignIn popup')
def click_signin_from_popup(context):
    context.app.header.click_signin_from_popup()


@when('wait for 3 sec')
def wait_sec(context):
    sleep(3)

@then('Verify Sign in is clickable')
def verifying_signin_btn_clickable(context):
    context.app.header.verify_signin_btn_clickable()

@then('Verify Sign in page opened')
def sign_in_page(context):
    context.app.sign_in_page.verify_signing_in_page()

@then ('Verify Sign in disappears')
def verifying_signin_btn_disappears(context):
    context.app.header.verify_signin_btn_disappear()


@then('Verify Email input field is present')
def email_input_field(context):
      context.app.sing_in_page.verify_email_input_field()