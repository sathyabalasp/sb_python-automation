from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


JEAN_COLOR_OPTIONS = (By.CSS_SELECTOR, '#variation_color_name li')
JEAN_CURRENT_COLOR = (By.CSS_SELECTOR, '#variation_color_name .selection')
@given('Open Amazon product {product_id} page')
def open_amazon_product(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@then('Verify user can click and see the colors of product')
def verify_clicking_colors(context):
    jean_colors = ['Black', 'Blue Over Dye', 'Dark Blue Vintage', 'Dark Indigo', 'Dark Wash', 'Indigo Wash',
                   'Light Wash', 'Medium Blue Vintage', 'Medium Wash', 'Rinsed', 'Vintage Wash', 'Washed Black',
                   'Bright White', 'Dark Khaki Brown', 'Light Khaki Brown', 'Olive', 'Light Blue Vintage',
                   'Washed Grey', 'Sage Green']
    actual_jean_colors = []

    colors = context.driver.find_elements(*JEAN_COLOR_OPTIONS)

    for color in colors[:]:
        color.click()
        current_jean_color = context.driver.find_element(*JEAN_CURRENT_COLOR).text

        actual_jean_colors.append(current_jean_color)

    assert actual_jean_colors == jean_colors, f'Expected {jean_colors} did not match actual {actual_jean_colors}'


