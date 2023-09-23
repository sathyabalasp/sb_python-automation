from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SEARCH_RESULT = (By.XPATH,'//span[@class ="a-color-state a-text-bold"]')
PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
SEARCH_RESULTS = (By.CSS_SELECTOR, "[data-component-type='s-search-result']")
PRODUCT_NAME = (By.CSS_SELECTOR, 'h2 span.a-text-normal')
PRODUCT_IMAGE = (By.CSS_SELECTOR, ".s-image[data-image-latency='s-product-image']")


# @when('Click on the first product')
# def click_first_product(context):
#      context.driver.find_element(*PRODUCT_PRICE).click()
#      sleep(2)

@when('Click on All Department dropdown')
def click_on_all_dropdown(context):
    context.app.header.click_on_all_dropdown()


@when('Select department by alias {dept}')
def select_dept(context, dept):
    context.app.header.select_dept(dept)


@then('Verify search result is {expected_result}')
def verify_search_result(context, expected_result):
     actual_result = context.driver.find_element(*SEARCH_RESULT).text
     assert expected_result == actual_result, f'Error, expected {expected_result} did not match actual {actual_result}'
     # context.app.search_result_page.verify_search_result(expected_result)


@then('Verify every product has a name and  an image')
def verify_products_name_img(context):
    all_products = context.driver.find_elements(*SEARCH_RESULTS)

    for product in all_products:
        product_name = product.find_element(*PRODUCT_NAME).text
        print(product_name)
        assert product_name, 'Product title not shown'
        product.find_element(*PRODUCT_IMAGE)


@then('Verify {dept} department is selected')
def verify_dept_selected(context, dept):
    context.app.header.verity_dept_selected(dept)
