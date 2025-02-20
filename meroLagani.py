#script to access to the live trading market and chsing a random company to check its price history in mero lagani 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://merolagani.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
market=driver.find_element(*(By.XPATH,"//a[normalize-space()='Market']"))
market.click()
time.sleep(2)
try:
    alert = Alert(driver)
    alert.dismiss()  # Dismiss the pop-up
except:
    print("No alert found")
live=driver.find_element(*(By.XPATH,"//a[normalize-space()='Live Trading']"))
live.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,400);")
time.sleep(2)
openLive=driver.find_element(*(By.XPATH,"//a[normalize-space()='ADBL']"))
openLive.click()
time.sleep(2)
#new tab opened so need to switch the mouse to the new tab 
driver.switch_to.window(driver.window_handles[1])  # Move to the new tab
time.sleep(2)
####
driver.execute_script("window.scrollBy(0,950);")
priceHistory=driver.find_element(*(By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lnkHistoryTab']"))
priceHistory.click()
time.sleep(2)
date=driver.find_element(*(By.XPATH,"//input[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_txtMarketDatePriceFilter']"))
date.send_keys("02/13/2023")
time.sleep(2)
search=driver.find_element(*(By.XPATH,"//a[@id='ctl00_ContentPlaceHolder1_CompanyDetail1_lbtnSearchPriceHistory']"))
search.click()
time.sleep(2)
driver.execute_script("window.scrollBy(0,100);")
# Close the browser after a short delay
time.sleep(5)
driver.quit()

