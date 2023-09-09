from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

JEAN_COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
JEAN_CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get('https://www.amazon.com/dp/{product_id}')
    sleep(3)
    context.driver.refresh()

@then('Verify user can click through colors')
def verify_clicking_colors(context):
    jean_colors = ['Light Wash', 'Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash', 'Indigo Wash',
                    'Medium Blue Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black',
                   'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown']
    actual_jean_colors = []

    colors = context.driver.find_elements(*JEAN_COLOR_OPTIONS)

    for color in colors[:]:
        color.click()
        current_jean_color = context.driver.find_element(*JEAN_CURRENT_COLOR).text

        actual_jean_colors.append(current_jean_color)

    assert actual_jean_colors == jean_colors, f'Expected {jean_colors} did not match actual {actual_jean_colors}'


