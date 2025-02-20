#file upload and download 
#script to upload and download in a demo web for file uploading filebin.net
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://filebin.net/"
driver.get(url)

# Close the browser after a short delay
driver.maximize_window()
fileSelector=driver.find_element(*(By.XPATH,"//input[@id='fileField']"))
#by reversing the location of file
# fileSelector.send_keys(r"C:\Users\Bhabisara Budhathoki\Desktop\convocation\convocation.png")
fileSelector.send_keys("C:/Users/Bhabisara Budhathoki/Desktop/convocation/convocation.png")
time.sleep(3)
more=driver.find_element(*(By.XPATH,"//a[@id='dropdownFileMenuButton']"))
more.click()
time.sleep(3)
download1=driver.find_element(*(By.XPATH,"//a[normalize-space()='Download file']"))
download1.click()
time.sleep(6)
driver.quit()
