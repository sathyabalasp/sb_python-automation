from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path='/Users/balamurugann/Automation_QA/sb_python-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.implicitly_wait(3)
driver.wait = WebDriverWait(driver, 3)
driver.get('https://www.amazon.com/')
driver.find_element(By.CSS_SELECTOR,"#nav-link-accountList[data-nav-role='signin']").click()

driver.find_element(By.CSS_SELECTOR,"#createAccountSubmit").click()

driver.find_element(By.CSS_SELECTOR,".a-icon.a-icon-logo")
driver.find_element(By.CSS_SELECTOR,'.a-spacing-small')
driver.find_element(By.CSS_SELECTOR,'#ap_customer_name')
driver.find_element(By.CSS_SELECTOR,'#ap_email')
driver.find_element(By.CSS_SELECTOR,'#ap_password')
driver.find_element(By.CSS_SELECTOR,'div.auth-inlined-information-message div.a-alert-content')
driver.find_element(By.CSS_SELECTOR,"#ap_password_check")
driver.find_element(By.CSS_SELECTOR,"#continue")
driver.find_element(By.CSS_SELECTOR,"a[href*='/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use']")
driver.find_element(By.CSS_SELECTOR,"a[href*='/gp/help/customer/display.html/ref=ap_register_notification_privacy_notice?']")
driver.find_element(By.CSS_SELECTOR,".a-link-emphasis[href*='/ap/signin?openid.pape.max_auth_age=0&openid.']")
print('Test Passed')

driver.quit()