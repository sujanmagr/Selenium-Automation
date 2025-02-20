# script for filling a admission form in website of mindrisers institute
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#get url
url="https://www.mindrisers.com.np/online-admission"
driver.get(url)
driver.maximize_window()
driver.execute_script("window.scrollBy(0, 850);")
#find id
name=driver.find_element(By.ID, "full_name")
email=driver.find_element(By.ID, "email")
phone=driver.find_element(By.ID, "mobile_no")
college=driver.find_element(By.ID, "college")
# Academic_status=driver.find_element(By.ID, "qualification")
status=driver.find_element(*(By.XPATH,"(//select[@id='qualification'])[1]"))
Course=driver.find_element(By.XPATH,("(//select[@id='course'])[1]"))
schedule=driver.find_element(By.XPATH, ("//select[@id='shedule']"))
yes=driver.find_element(By.ID, "remarks-yes")
Queries=driver.find_element(By.ID, "question")

# captcha=driver.find_element(By.XPATH,("//div[@class='recaptcha-checkbox-border']"))
#enter values
name.send_keys("sachin")
email.send_keys("budhathoki12@gmail.com")
phone.send_keys("9876543215")
college.send_keys("Nepalaya")
#select academic statud
select=Select(status)
select.select_by_index(1)
# select course
select=Select(Course)
select.select_by_index(2)
# select Schedule
select=Select(schedule)
select.select_by_index(2)
#enter queries
Queries.send_keys("Good courses")
# captcha.click()
time.sleep(5)
driver.quit()

