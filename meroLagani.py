#script to access to the live trading market and chsing a random company to check its price history in mero lagani 
# Importing required libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

# Setting up Chrome WebDriver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Open Mero Lagani
driver.get("https://merolagani.com/")
driver.maximize_window()
time.sleep(2)

# Navigate to Market & Live Trading
driver.find_element(By.XPATH, "//a[normalize-space()='Market']").click()
time.sleep(2)

# Handling pop-up alerts
try:
    alert = Alert(driver)
    alert.dismiss()
except:
    print("No alert found")

driver.find_element(By.XPATH, "//a[normalize-space()='Live Trading']").click()
time.sleep(2)

# Scroll down & Open a company
driver.execute_script("window.scrollBy(0,400);")
driver.find_element(By.XPATH, "//a[normalize-space()='ADBL']").click()
time.sleep(2)

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Scroll & Access Price History
driver.execute_script("window.scrollBy(0,950);")
driver.find_element(By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']").click()
time.sleep(2)

# Enter date & search price history
date_input = driver.find_element(By.XPATH, "//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']")
date_input.send_keys("02/13/2022")

search = driver.find_element(By.XPATH, "//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lbtnSearchPriceHistory']")
search.click()
time.sleep(2)

# Scroll & View Results
driver.execute_script("window.scrollBy(0,100);")

# Closing browser
time.sleep(5)
driver.quit()
