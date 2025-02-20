#script to login into mero share login page 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
# Open a webpage to test
url="https://meroshare.cdsc.com.np/#/login"
driver.get(url)

# Close the browser after a short delay
driver.maximize_window()
time.sleep(2)
dp=driver.find_element(By.XPATH,"/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[1]/div/div/select2/span/span[1]/span/span[1]/span")
dp.click()
dpSelect=driver.find_element(By.XPATH, "/html/body/span/span/span[2]/ul/li[2]")
dpSelect.click()
username= driver.find_element(*(By.XPATH,"//input[@id='username']"))
password=driver.find_element(By.ID, "password")
password.send_keys("sachin")
username.send_keys("1234253617")
login1=driver.find_element(By.XPATH, "/html/body/app-login/div/div/div/div/div/div/div[1]/div/form/div/div[4]/div/button")
login1.click()
time.sleep(4)
driver.quit()
