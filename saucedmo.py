# script to login into a login page of saucedemo with certain users and password
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# setting the url to a variable
url="https://www.saucedemo.com/"
driver.get(url)
driver.maximize_window()
time.sleep(2)
#find the input fields 
username=driver.find_element(By.ID, "user-name")# using id selector
password=driver.find_element(*(By.XPATH,"//input[@id='password']"))# using xpath selector
login=driver.find_element(By.ID, "login-button")
#enter username and password
username.send_keys("standard_user")
password.send_keys("secret_sauc")
time.sleep(3)
login.click()
# to test wheather login successful or not
title=driver.current_url
if (title=="https://www.saucedemo.com/inventory.html"):
    print("login successful")
else:
    print("login unsuccessful")

time.sleep(5)
driver.quit()
