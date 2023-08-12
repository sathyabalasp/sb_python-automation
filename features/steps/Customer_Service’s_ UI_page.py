from behave import given, when, then
from selenium.webdriver.common.by import By
from time import sleep
CUSTOMER_SERVICE_PAGE =(By.CSS_SELECTOR,'a[href="/gp/help/customer/display.html?nodeId=508510&ref_=nav_cs_customerservice"]')
WELCOME_CUSTOMER = (By.CSS_SELECTOR,'.fs-heading.bolded')
ISSUE_CARD = (By.CSS_SELECTOR,'.issue-card-container')
ISSUE_CARD_UI_ELEMENTS = (By.CSS_SELECTOR,'.issue-card-wrapper')
ALL_HELP_TOPICS_UI_ELEMENTS = (By.CSS_SELECTOR,'.help-topics')
SEARCH_OUR_HELP_LIBRARY = (By.XPATH,'//h2[text()="Search our help library"]')
INPUT_SEARCH_OUR_HELP_LIBRARY = (By.CSS_SELECTOR,'#hubHelpSearchInput')
ALL_HELP_TOPICS = (By.XPATH,'//h2[text()="All help topics"]')

@given('Open Amazon Customer Service page')
def Customer_Service(context):
    context.driver.find_element(*CUSTOMER_SERVICE_PAGE).click()
    context.driver.find_element(*WELCOME_CUSTOMER)

@when('Check for in issue card UI elements')
def issue_card_ui_elements(context):
    context.driver.find_element(*ISSUE_CARD)
    context.driver.find_elements(*ISSUE_CARD_UI_ELEMENTS)


@then('Check for in Search our help library UI elements')
def search_help_library_elements(context):
    context.driver.find_element(*SEARCH_OUR_HELP_LIBRARY)
    context.driver.find_element(*INPUT_SEARCH_OUR_HELP_LIBRARY)
    context.driver.find_element(*ALL_HELP_TOPICS_UI_ELEMENTS)


@then('Verify UI  no of {no_link} elements')
def verify_no_ui_links(context, no_link):
    no_link = int(no_link)
    no_of_link = context.driver.find_elements(*ISSUE_CARD_UI_ELEMENTS)
    assert len(no_of_link) == no_link, f'error,no of UI elements {no_link} but there is only {len(no_of_link)}'


@then('Verify other UI links {no_link2} elements')
def verify_all_help_topic_ui(context, no_link2):
    no_link2 = int(no_link2)
    no_of_link1 = context.driver.find_elements(*ALL_HELP_TOPICS_UI_ELEMENTS)
    assert len(no_of_link1) == no_link2, f'error,no of UI elements {no_link2} but there is only {len(no_of_link1)}'


