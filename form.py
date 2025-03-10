#script to fillup a form in formy.com
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url="https://formy-project.herokuapp.com/form"
driver.get(url)
driver.maximize_window()
#find input fields
firstName=driver.find_element(By.ID, "first-name")
lastName=driver.find_element(By.ID, "last-name")
job=driver.find_element(By.ID, "job-title")
EducationLevel=driver.find_element(By.ID, "radio-button-1")
gender=driver.find_element(By.ID, "checkbox-1")
year=driver.find_element(By.ID, "select-menu")
experience=driver.find_element(By.XPATH, "/html/body/div/form/div/div[6]/select/option[4]")
date=driver.find_element(By.XPATH,"//input[@id='datepicker']")
#send data to the input fields
firstName.send_keys("sujan")
lastName.send_keys("magar")
job.send_keys("Student")
EducationLevel.click()
gender.click()
time.sleep(5)
#scroll down
driver.execute_script("window.scrollBy(0, 300);")
year.click()
experience.click()
date.send_keys("22/04/2022")
time.sleep(3)

time.sleep(4)
driver.quit()
