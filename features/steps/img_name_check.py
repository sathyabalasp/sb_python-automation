from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_NAMES = (By.CSS_SELECTOR,'span.a-size-base-plus.a-color-base.a-text-normal')
PRODUCT_IMAGE = (By.CSS_SELECTOR,'div.a-section.aok-relative.s-image-square-aspect img.s-image')

@then('Verify every product has name and image')
def verifying_product_name_and_image(context):
    product_name = []
    product_image = []

    names = context.driver.find_elements(*PRODUCT_NAMES).text
    
    for name in names[:24]:

        current_name = name
        product_name.append(current_name)
        current_image = context.driver.find_element(*PRODUCT_IMAGE).get_attribute(product_image)
        product_image.append(current_image)

    print(product_name)