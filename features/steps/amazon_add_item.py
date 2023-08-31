from behave import given, when, then
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC


@when('Input the product')
def enter_product_name(context):
    context.app.header.search_product('cell phone')


@then('Select one product')
def select_product(context):
    context.app.header.click_select_product()


@then('Add it to the cart')
def adding_to_cart(context):
    context.app.search_result_page.add_product_to_cart()


@then('Verify {exp_text} number of present')
def verify_number_product_in_cart(context,exp_text):
    context.app.search_result_page.verify_number_of_items_in_cart(exp_text)
