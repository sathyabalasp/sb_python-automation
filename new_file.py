from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


# create a new Chrome browser instance
service = Service(executable_path='/Users/balamurugann/Automation_QA/sb_python-automation/chromedriver')
driver = webdriver.Chrome(service=service)
driver.maximize_window()

driver.get('https://www.amazon.com/')

driver.find_element(By.ID, 'nav-search-submit-button')
driver.find_element(By.ID, 'nav-cart-count')




driver.find_element(By.XPATH, "//a[@data-csa-c-content-id='nav_cs_bestsellers']")
driver.find_element(By.XPATH, "//input[@aria-label='Search Amazon']")

# Multiple attributes
driver.find_element(By.XPATH, "//a[@class='nav-a  ' and @data-csa-c-content-id='nav_cs_bestsellers']")

# By Xpath, text
driver.find_element(By.XPATH, "//a[text()='Best Sellers']")
driver.find_element(By.XPATH, "//a[text()='Best Sellers' and @class='nav-a  ']")

# Any tag = *
driver.find_element(By.XPATH, "//*[text()='Best Sellers' and @class='nav-a  ']")

# Contains
driver.find_element(By.XPATH, "//a[contains(@href, 'nav_cs_bestsellers')]")
driver.find_element(By.XPATH, "//a[contains(text(), 't Seller') and @class='nav-a  ']")


driver.find_element(By.XPATH, "//div[@id='nav-belt']//input[@placeholder='Search Amazon']")
