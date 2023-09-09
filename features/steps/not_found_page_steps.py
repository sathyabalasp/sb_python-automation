from behave import *


@given('Store original windows')
def store_original_windows(context):
    context.original_window = context.app.not_found_page.store_original_window()

@when('Click on Dog image')
def click_dog_imgs(context):
    context.app.not_found_page.click_dog_img()


@when('Switch to new window')
def switch_to_new_windows(context):
    context.app.not_found_page.switch_to_new_window()


