from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger

 # behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/bestsellers.feature

def browser_init(context):
# def browser_init(context, scenario_name):  # add scenario_name if you want to use it in Browserstack
    """
    :param context: Behave context
    """

    service = Service(executable_path='/Users/balamurugann/Automation_QA/sb_python-automation/chromedriver')
    context.driver = webdriver.Chrome(service=service)
    context.driver.maximize_window()
    ### OTHER BROWSERS ###
    # service = Service(executable_path='/Users/balamurugann/Automation_QA/sb_python-automation/geckodriver')
    # context.driver = webdriver.Firefox(service=service)
    # context.driver = webdriver.Safari()

    # HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # service = Service(executable_path='/Users/balamurugann/Automation_QA/sb_python-automation/chromedriver')
    # context.driver = webdriver.Chrome(options=options, service=service)

    ## BROWSERSTACK ###
    # # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settingspip3 install -r requirements.txt
    # bs_user = 'sathyaprabhasoun_cKy6sq'
    # bs_key = 'Co5KS7YR3GDYPpYi8Hkc'
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    #
    # options = Options()
    # bstack_options = {
    #     "os": "OS X",
    #     "osVersion": "Monterey",
    #     "browserName": "Chrome",
    #     "browserVersion": "latest",
    #     "browserstackLocal": "true",
    #     "buildName": "browserstack-build-1",
    #     "projectName": "BrowserStack Sample",
    #     "sessionName": "scenario_name"
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)

    context.app = Application(context.driver)

def before_scenario(context, scenario):

    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context)
    # browser_init(context, scenario.name)

def before_step(context, step):
    print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
        logger.error(f'Step failed: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()

